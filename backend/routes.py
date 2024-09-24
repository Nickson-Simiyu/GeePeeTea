import bcrypt
from flask import Blueprint, flash, redirect, render_template, request, url_for
from forms import LoginForm, RegistrationForm
from models import Parent, Person, Teacher, Student, db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/login-parent', methods=['GET', 'POST'])
def parent_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if form.role.data == 'parent':
                # Handle parent login logic
                flash('Login successful as Parent!', 'success')
                return redirect(url_for('main.parent_dashboard'))  # Example redirect
            elif form.role.data == 'teacher':
                # Handle teacher login logic
                flash('Login successful as Teacher!', 'success')
                return redirect(url_for('main.teacher_dashboard'))  # Example redirect
            elif form.role.data == 'student':
                # Handle student login logic
                flash('Login successful as Student!', 'success')
                return redirect(url_for('main.student_dashboard'))  # Example redirect
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')

    return render_template("/templates/login.html", form=form)

@main.route('/login-teacher', methods=['GET', 'POST'])
def teacher_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if form.role.data == 'parent':
                # Handle parent login logic
                flash('Login successful as Parent!', 'success')
                return redirect(url_for('main.parent_dashboard'))  # Example redirect
            elif form.role.data == 'teacher':
                # Handle teacher login logic
                flash('Login successful as Teacher!', 'success')
                return redirect(url_for('main.teacher_dashboard'))  # Example redirect
            elif form.role.data == 'student':
                # Handle student login logic
                flash('Login successful as Student!', 'success')
                return redirect(url_for('main.student_dashboard'))  # Example redirect
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')

    return render_template("/templates/login.html", form=form)

@main.route('/login-parent', methods=['GET', 'POST'])
def student_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if form.role.data == 'parent':
                # Handle parent login logic
                flash('Login successful as Parent!', 'success')
                return redirect(url_for('main.parent_dashboard'))  # Example redirect
            elif form.role.data == 'teacher':
                # Handle teacher login logic
                flash('Login successful as Teacher!', 'success')
                return redirect(url_for('main.teacher_dashboard'))  # Example redirect
            elif form.role.data == 'student':
                # Handle student login logic
                flash('Login successful as Student!', 'success')
                return redirect(url_for('main.student_dashboard'))  # Example redirect
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')

    return render_template("/templates/login.html", form=form)

@main.route('/register-parent', methods=['GET', 'POST'])
def register_parent():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process the form data (e.g., save to the database)
        flash('Registration successful!', 'success')
        return redirect(url_for('main.home'))  # Redirect to home or login page

    return render_template('register-parent.html', form=form)

@main.route('/register-teacher', methods=['GET', 'POST'])
def register_teacher():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process the form data (e.g., save to the database)
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))  # Redirect to home or login page

    return render_template('register-teacher.html', form=form)

@main.route('/register-student', methods=['GET', 'POST'])
def register_student():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process the form data (e.g., save to the database)
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))  # Redirect to home or login page

    return render_template('register-student.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Person.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if form.role.data == 'parent':
                # Handle parent login logic
                flash('Login successful as Parent!', 'success')
                return redirect(url_for('main.parent_dashboard'))  # Example redirect
            elif form.role.data == 'teacher':
                # Handle teacher login logic
                flash('Login successful as Teacher!', 'success')
                return redirect(url_for('main.teacher_dashboard'))  # Example redirect
            elif form.role.data == 'student':
                # Handle student login logic
                flash('Login successful as Student!', 'success')
                return redirect(url_for('main.student_dashboard'))  # Example redirect
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')

    return render_template("/templates/login.html", form=form)


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


@main.route('/next')
def back():
    return render_template("parent/register-parent.html")

@main.route('/next1')
def back2():
    return render_template("student/register-student.html")

@main.route('/next2')
def back3():
    return render_template("register.html")


@main.route('/parent')
def parent_dashboard():
    return render_template('parent/dashboard.html')

@main.route('/teacher')
def teacher_dashboard():
    return render_template('teacher/dashboard.html')

@main.route('/student')
def student_dashboard():
    return render_template('student/dashboard.html')