from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Person(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Parent(Person):
    __tablename__ = 'parents'


class Teacher(Person):
    __tablename__ = 'teachers'


class Student(Person):
    __tablename__ = 'students'
