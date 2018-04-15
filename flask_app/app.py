from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from pprint import pprint
import json

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hushushs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:3306/flaskwtftest'.format('root','')

# declare exetensions
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# SQLAlchemy Model
class BlogModel(db.Model):
	__tablename__ = 'blog'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	slug = db.Column(db.String(255), nullable=False)
	content = db.Column(db.Text, nullable=False)

# WTForms
class BlogForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	slug = StringField('Slug', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('kirim')

# Routes
@app.route('/')
def hello_world():
	form = BlogForm()
	return render_template('blogForm.html', form=form)

@app.route('/blog/create', methods=['GET','POST'])
def blog_create():
	form = BlogForm()
	if(form.validate_on_submit()):
		blog = BlogModel()
		form.populate_obj(blog)
		db.session.add(blog)
		db.session.commit()
		return 'oke'
	return render_template('blogForm.html', form=form)