from flask import Flask
from .extensions import db
from .configs import DevConfig
from flask_app import blog

def create_app():
	app = Flask(__name__)
	register_extensions(app)
	register_blueprint(app)
	return app;

def register_extensions(app):
	db.init_app(app)
	return app

def register_blueprint(app):
	app.register_blueprint(blog.views.blueprint)
	return app