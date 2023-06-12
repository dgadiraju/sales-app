from flask import render_template, request
from app import app
from app import db
from models.user import User


@app.route('/users')
def users():
    user_recs = db.session.query(User).all()
    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users=users)


@app.route('/user', methods=['GET'])
def user():
    id = request.args.get('id')
    user = User.query.get(id)
    return render_template('user_detail.html', user=user)
