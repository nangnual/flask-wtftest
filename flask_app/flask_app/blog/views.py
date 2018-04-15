from flask import Blueprint, render_template

blueprint = Blueprint('blog', __name__, url_prefix='/blog', static_folder='./static')

@blueprint.route('/create')
def create():
	return 'blog.create'