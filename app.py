from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)
from models.user import User


@app.route('/')
def hello_world():
    # rec = db.get_or_404(User, 1)
    rec = User.query.get_or_404(1)
    return f'<p>Hello, World! from {rec.username}</p>'
