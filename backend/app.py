from flask import Flask
from routes import main
from jinja2 import ChoiceLoader, FileSystemLoader

app = Flask(__name__, static_folder='../css')

app.jinja_loader = ChoiceLoader([
    FileSystemLoader('../templates'),
    FileSystemLoader('../templates/parent'),
    FileSystemLoader('../templates/teacher'),
    FileSystemLoader('../templates/student')
])

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)