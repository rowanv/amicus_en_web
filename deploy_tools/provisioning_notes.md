Provisioning the dashboard
==========================

## Required packages:

* nginx
* Python 3
* Git
* Pip
* virtualenv

e.g., on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with domain name, e.g. staging.my-domain.com


# Automated deploy
## on my machine

fab deploy --host=rowan@amicus-vet.net
scp ../config.yml rowan@159.203.117.177:~/sites/amicus-vet.net/source/


## Then on the actual server, within source for the website

sed "s/SITENAME/dash.rowanv.com/g" \
    deploy_tools/nginx.template.conf | sudo tee \
    /etc/nginx/sites-available/amicus-vet.net

sudo ln -s ../sites-available/amicus-vet.net \
    /etc/nginx/sites-enabled/amicus-vet.net

sed "s/SITENAME/dash.rowanv.com/g" \
    deploy_tools/gunicorn-upstart.template.conf | sudo tee \
    /etc/init/gunicorn-amicus-vet.net.conf

sudo service nginx reload
#sudo start gunicorn-amicus-vet.net
# or once have started:
sudo restart gunicorn-amicus-vet.net
# Actually, currently starting gunicorn with:
# ../virtualenv/bin/gunicorn -w 4 -b 0.0.0.0:5000 run:app -D
# To view running gunicorn processes:
# ps ax|grep gunicorn
