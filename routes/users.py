from flask import render_template, request, \
    redirect, url_for
from app import app
from app import db
from models.user import User


@app.route('/users')
def users():
    user_recs = db.session.query(User).all()
    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users=users)


@app.route('/user', methods=['GET', 'POST'])
def user():
    id = request.args.get('id')
    if request.method == 'GET':
        if id:
            user = User.query.get(id)
            return render_template('user_detail.html', user=user)
        else:
            return render_template('user_form.html')
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))
