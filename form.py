from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField
from wtforms.validators import data_required, Length,Email, EqualTo


class RegistrationForm(FlaskForm):

    '''form username'''
    username = StringField('Username', validators=[data_required(), Length(min=2, max=20) ])
    '''Form email'''
    email = StringField('Email', validators=[data_required(), Email()])
    '''Form password'''
    password = PasswordField('Password', validators=[data_required()])

    confirm_password = PasswordField('Confirm Password', validators=[data_required(), EqualTo('password')])

    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):

    '''Form email'''
    email = StringField('Email', validators=[data_required(), Email()])
    '''Form password'''
    password = PasswordField('Password', validators=[data_required()])

    remember = BooleanField('Remember me')
  
    submit = SubmitField('Log in')
