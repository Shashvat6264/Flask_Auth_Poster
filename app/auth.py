from flask import Blueprint, render_template, url_for, request, redirect, flash
from forms import RegForm, LoginForm
from models import Person,db
from flask_login import login_user, current_user, login_required, logout_user

auth_blueprint = Blueprint('auth_blueprint',__name__, template_folder='templates',static_folder='static')

@auth_blueprint.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    try: 
        if current_user.is_authenticated:
            return redirect(url_for("main_blueprint.profile"))
    except:
        pass
    if form.validate_on_submit():
        try:
            user = Person.query.filter_by(username=form.username.data).first()
            if form.password.data==user.password:
                    login_user(user)
                    return redirect(url_for("main_blueprint.profile"))
            else:
                return render_template('Loginform.html', form=form)    
        except:
            return render_template('Loginform.html', form=form)
    return render_template('Loginform.html', form=form)

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')

@auth_blueprint.route('/signup')
def signup():
    form = RegForm()
    return render_template('regform.html', form=form)

@auth_blueprint.route('/registered', methods=['POST','GET'])
def registered():
    user = Person.query.filter_by(username=request.form['username']).first()
    if user != None:
        redirect(url_for("auth_blueprint.login"))
    else:
        pf = Person(request.form['name'],request.form['username'], request.form['password'])
        db.session.add(pf)
        db.session.commit()
        print('User Registered')
        login_user(pf)
        return render_template('registered.html')