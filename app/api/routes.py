from flask import Blueprint, jsonify
from app.models import db
from app.models.radwomen import Radwoman


api = Blueprint("api", __name__)


@api.route("/radwomen")
def index():
	try:
		women = db.session.query(Radwoman).all()
		toReturn = [{'name': rad.wiki_name} for rad in women]
		return jsonify({'women':toReturn}), 200
	except Exception as e:

		raise(e)
		return jsonify({'error': 'transaction error'}), 500