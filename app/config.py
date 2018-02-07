import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "radwomen.db")

DATABASE_NAME = 'radwomen.db'
ABS_PATH = '/home/ondoheer/projects/python_projects/radwomen-api/'
class BaseConfig(object):

	DEBUG = False


class DevConfig(BaseConfig):

	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///{}{}".format(ABS_PATH, DATABASE_NAME)
	# SQLALCHEMY_DATABASE_URI = 'postgresql://ondoheer:@localhost/radwomen'
	SECRET_KEY = "mellon"