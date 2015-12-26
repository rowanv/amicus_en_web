from flask import Flask, render_template, request
from flask.ext.babel import Babel
from config import LANGUAGES


app = Flask(__name__)
babel = Babel(app)

import logging
from logging import FileHandler
file_handler = FileHandler('debug.log', 'a')
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up/')
def sign_up():
    return render_template('sign_up.html')

@app.route('/pricing/')
def pricing():
    return render_template('pricing_table.html')

@app.route('/paypal/')
def paypal():
    return render_template('paypal.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
