import bcrypt
from flask import Blueprint, flash, redirect, render_template, request, url_for
from models import Parent, Teacher, Student, db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/next')
def back():
    return render_template("parent/register-parent.html")

@main.route('/next1')
def back2():
    return render_template("student/register-student.html")

@main.route('/next2')
def back3():
    return render_template("teacher/login-teacher.html")



@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login successful!', 'success')
            # Redirect to a protected route (e.g., user's dashboard)
            return redirect(url_for('main.index'))  # Ensure 'main.index' is the correct route for the dashboard
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')

    return render_template("/templates/login.html", form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.login'))
    return redirect('/templates/login.html', form=form)


@main.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')

    if username and email:
        new_user = Parent(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
    else:
        flash('Please provide username and email.', 'danger')

    return redirect(url_for('main.home'))

