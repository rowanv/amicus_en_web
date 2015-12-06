from run import app as application
from werkzeug.contrib.fixers import ProxyFix

application.wsgi_app = ProxyFix(application.wsgi_app)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
