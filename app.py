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
    user_recs = db.session.query(User).all()
    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users=users)
