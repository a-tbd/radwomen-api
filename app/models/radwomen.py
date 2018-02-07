from app.models import db

class Radwoman(db.Model):

	__tablename__ = 'radwomen'

	id = db.Column(db.Integer, primary_key=True)
	wiki_name = db.Column(db.String(80), unique=True, nullable=False)
	wiki_link = db.Column(db.String(255))

	def __init__(self, name):
		self.wiki_name = name


	def __repr__(self):
		return f"<Radwoman {self.wiki_name} at {self.wiki_link}>"