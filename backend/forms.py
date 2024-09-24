from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    role = RadioField('Role', choices=[('parent', 'Parent'), ('teacher', 'Teacher'), ('student', 'Student')], default='student', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = RadioField('Role', choices=[('parent', 'Parent'), ('teacher', 'Teacher'), ('student', 'Student')], default='student', validators=[DataRequired()])
    submit = SubmitField('Sign In')
