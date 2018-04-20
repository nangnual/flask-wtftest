from flask import Blueprint, render_template

blueprint = Blueprint('blog', __name__, url_prefix='/blog', template_folder = 'templates')

@blueprint.route('/create')
def create():
	# return blueprint.root_path
	return render_template('something.html')
	return 'blog.create'