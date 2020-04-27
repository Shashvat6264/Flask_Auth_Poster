from flask import Blueprint, render_template, url_for, request
from models import Post,db, Person
import pickle
from flask_login import login_required, current_user

main_blueprint = Blueprint('main_blueprint', __name__,template_folder='templates',static_folder='static')

@main_blueprint.route("/", methods=['POST','GET'])
def index():
    return render_template('index.html')

@main_blueprint.route("/profile", methods=['POST','GET'])
@login_required
def profile():
    posts = Post.query.all()
    return render_template("profile.html",user=current_user,posts=posts)

@main_blueprint.route("/liked",methods=['POST','GET'])
@login_required
def liked():
    if request.method == 'POST':
        content = request.get_json()
        id = content['id']
        p = Post.query.filter_by(id=id).first()
        l = pickle.loads(p.likers)
        if current_user.username not in l:
            p.likes += 1
            l.append(current_user.username)
            p.likers = pickle.dumps(l)
            db.session.commit()
        return 'Liked'
    else:
        return None

@main_blueprint.route("/profile/<username>")
@login_required
def profile_view(username):
    p = Person.query.filter_by(username=username).first()
    return render_template("profile_view.html",person=p)