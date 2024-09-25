import bcrypt
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_required, logout_user
from forms import LoginForm, RegistrationForm
from models import Parent, Person, Teacher, Student, db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

# Registration
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Person(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.login'))
    return render_template("main.register", form=form)

#Login
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Save user info in the session
            session['user_id'] = user.id
            session['email'] = user.email
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')
    return render_template("main.login", form=form, category='error')

# Logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("/")


# USER ROUTES

# Parent
@main.route('/register-parent')
def parent_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Person(fullname=form.fullname.data, student_name=form.student_name.data, mail=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.parent_login'))
    return render_template("main.parent_register", form=form)

@main.route('/login-parent', methods=['GET', 'POST'])
def parent_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(fullname=form.fullname.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Save user info in the session
            session['user_id'] = user.id
            session['fullname'] = user.fullname
            flash('Login successful!', 'success')
            return redirect(url_for('main.parent_dashboard'))
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')
    return render_template("main.parent_login", form=form, category='error')

@main.route('/parent')
#@login_required
def parent_dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('main.parent_login'))
    return render_template('parent/dashboard.html')



# Teacher
@main.route('/register_teacher', methods=['GET', 'POST'])
def teacher_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Person(fullname=form.fullname.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.teacher_login'))
    return render_template("main.teacher_register", form=form)

@main.route('/register_login', methods=['GET', 'POST'])
def teacher_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(fullname=form.fullname.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Save user info in the session
            session['user_id'] = user.id
            session['fullname'] = user.fullname
            flash('Login successful!', 'success')
            return redirect(url_for('main.teacher_dashboard'))
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')
    return render_template("main.teacher_login", form=form, category='error')

@main.route('/teacher', methods=['GET', 'POST'])
#@login_required
def teacher_dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('main.teacher_login'))
    return render_template('teacher/teacher.html')



# Student
@main.route('/register-student', methods=['GET', 'POST'])
def student_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Person(fullname=form.fullname.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.student_login'))
    return render_template("main.student_register", form=form)

@main.route('/login-student', methods=['GET', 'POST'])
def student_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(fullname=form.fullname.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Save user info in the session
            session['user_id'] = user.id
            session['fullname'] = user.fullname
            flash('Login successful!', 'success')
            return redirect(url_for('main.student_dashboard'))
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')
    return render_template("main.student_login", form=form, category='error')

@main.route('/student', methods=['GET', 'POST'])
#@login_required
def student_dashboard():
    #if 'user_id' not in session:
    #    flash('Please log in to access this page.', 'warning')
    #    return redirect(url_for('main.student_login'))
    return render_template('student/student.html')

@main.route('/student/pastpapers', methods=['GET', 'POST'])
def pastpapers():
    return render_template('student/pastpapers.html')

@main.route('/student/e-learning', methods=['GET', 'POST'])
def e_learning():
    return render_template('student/e-learning.html')

@main.route('/student/syllabus', methods=['GET', 'POST'])
def syllabus():
    return render_template('student/syllabus.html')