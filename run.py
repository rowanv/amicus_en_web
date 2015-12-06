from flask import Flask, render_template
from flask.ext.babel import babel
from config import LANGUAGES


app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up/')
def sign_up():
    return render_template('sign_up.html')

if __name__ == '__main__':
    app.run()