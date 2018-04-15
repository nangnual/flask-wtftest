# Contains all configuration/setting for this app
# like SECRET, SQL_ALCHEMY_DATABASE_URI, etc

import os

class Config(object):
	SECRET_KEY = 'mbuhlah'
	SQL_ALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@localhost:3306/flaskwtftest'.format('root','')

class DevConfig(Config):
	DEBUG = True
	ENV = 'dev'
