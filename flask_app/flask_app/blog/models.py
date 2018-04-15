from .extensions import db

class BlogModel(db.Model):
	__tablename__ = 'blog'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	slug = db.Column(db.String(255), nullable=False)
	content = db.Column(db.Text, nullable=False)