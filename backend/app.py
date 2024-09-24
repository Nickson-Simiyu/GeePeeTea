from flask import Flask, send_from_directory
from models import db
from routes import main
from jinja2 import ChoiceLoader, FileSystemLoader

app = Flask(__name__, static_folder='../css')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

app.jinja_loader = ChoiceLoader([
    FileSystemLoader('../templates'),
    FileSystemLoader('../templates/parent'),
    FileSystemLoader('../templates/teacher'),
    FileSystemLoader('../templates/student')
])

# Serve JS from the /js directory
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('../js', filename)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)