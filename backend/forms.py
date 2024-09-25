from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = RadioField('Role', choices=[('parent', 'Parent'), ('teacher', 'Teacher'), ('student', 'Student')], default='student', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('Register')
    
    def validate(self):
        # Call the parent class validate method
        if not super(RegistrationForm, self).validate():
            return False
        
        # Custom validation logic here (if needed)
        if self.password.data != self.confirm_password.data:
            self.password.errors.append("Passwords must match.")
            return False
        
        return True
