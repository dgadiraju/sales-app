from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)
from models.user import User


@app.route('/')
def hello_world():
    # rec = db.get_or_404(User, 1)
    rec = User.query.get_or_404(1)
    return render_template('index.html', user=rec)


@app.route('/users')
def users():
    users = [
        {'id': 1, 'first_name': 'Scott', 'last_name': 'Tiger', 'username': 'stiger', 'email': 'stiger@email.com'},
        {'id': 2, 'first_name': 'Mickey', 'last_name': 'Mouse', 'username': 'mmouse', 'email': 'mmouse@email.com'},
        {'id': 3, 'first_name': 'Charlie', 'last_name': 'Chaplin', 'username': 'cchaplin', 'email': 'cchaplin@email.com'}
    ]
    return render_template('users.html', users=users)
