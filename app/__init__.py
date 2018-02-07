from flask import Flask 

from app.models import db

from app.api.routes import api



def create_app(config='DevConfig'):

	app = Flask(__name__)

	app.config.from_object("app.config.{}".format(config))

	# instantiate blueprints
	app.register_blueprint(api)
	# instantiate extensions
	db.init_app(app)
	
	# db.create_all()
	return app

