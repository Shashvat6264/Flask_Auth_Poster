from flask import Blueprint, render_template, url_for, request
from forms import PostAdd
from models import Post,db
import pickle
from flask_login import login_required, current_user

post_blueprint = Blueprint('post_blueprint', __name__,template_folder='templates',static_folder='static')

@post_blueprint.route("/add_post", methods=['POST','GET'])
@login_required
def add_post():
    form = PostAdd()
    return render_template('Postform.html',form=form)

@post_blueprint.route("/post_added", methods=['POST','GET'])
@login_required
def all_posts():
    pf = Post(request.form['description'],request.form['complete_post'], current_user.username, 1)
    current_user.posts.append(pf)
    pf.likers = pickle.dumps([current_user.username])
    db.session.add(pf)
    db.session.commit()
    return render_template('posted.html')