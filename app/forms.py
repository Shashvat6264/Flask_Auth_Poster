from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField,SubmitField
from wtforms.validators import DataRequired

class RegForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostAdd(FlaskForm):
    description = StringField('Description',validators=[DataRequired()])
    complete_post = StringField('Complete Post',validators=[DataRequired()])
    submit = SubmitField('Submit')