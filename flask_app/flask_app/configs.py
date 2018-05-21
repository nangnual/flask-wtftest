# Contains all configuration/setting for this app
# like SECRET, SQL_ALCHEMY_DATABASE_URI, etc

import os

class Config(object):
	SECRET_KEY = 'mbuhlah'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@localhost:3306/flaskwtftest'.format('root','')
	EXPLAIN_TEMPLATE_LOADING = 1

class DevConfig(Config):
	DEBUG = True
	ENV = 'dev'

class TestConfig(Config):
	DEBUG = True
	TESTING = True
