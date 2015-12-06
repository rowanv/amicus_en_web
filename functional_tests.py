import unittest
from flask import Flask
from flask.ext.testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen

from run import app


class StylingAndStatusCode(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.close()


    def test_index_returns_200_code(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_sign_up_returns_200_code(self):
        response = urlopen(self.get_server_url() + '/sign_up/')
        self.assertEqual(response.code, 200)

    def test_layout_and_styling(self):
        self.driver.get(self.get_server_url())
        self.driver.set_window_size(1024, 768)

        header = self.driver.find_element_by_class_name('services')
        header_color = header.value_of_css_property('color')
        self.assertEqual(header_color, 'rgba(255, 255, 255, 1)')

    def tearDown(self):
        self.driver.close()

class NewUserTest(LiveServerTestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def test_new_user_can_visit_sign_up_page(self):
        self.driver.get(self.get_server_url())
        self.driver.find_element_by_id('button_sign_up').click()

        # And the sign-up box appears
        self.driver.find_element_by_id('mc_embed_signup')
        self.assertEqual(self.driver.find_element_by_id('mce-FNAME').text,
                        'First Name')

    def new_user_can_click_through_navigation(self):
        # Our new user has heard of a new app.
        # They arrive at the home page and click on the 'about' link
        self.driver.get(self.get_server_url())
        self.driver.find_element_by_id('menu-toggle').click()

        self.driver.find_element_by_id('nav-about').click()

        #they go back to the top by clicking on the toggle, home

        self.driver.find_element_by_id('menu-toggle').click()
        self.driver.find_element_by_id('nav-home').click()

        #they go to why choose by clicking on the toggle, why choose
        self.driver.find_element_by_id('menu-toggle').click()
        self.driver.find_element_by_id('nav-why-choose').click()

        # they go to features by clicking on toggle, features
        self.driver.find_element_by_id('menu-toggle').click()
        self.driver.find_element_by_id('features').click()

        # they go to try it now by clicking on the toggle, try it now
        self.driver.find_element_by_id('menu-toggle').click()
        self.driver.find_element_by_id('try-it-now').click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()