# Contains all extensions this app uses
# and initialize those extension, so the app_aggregator
# can register the extensions to the app

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm

db = SQLAlchemy()
