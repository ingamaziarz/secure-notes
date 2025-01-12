from flask import Flask
import sqlite3
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwertyuiojhgfdscvbnm'
    app.config['DATABASE'] = os.path.join(app.instance_path, 'notes.db')

    from .routes import routes
    from .auth import auth

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app