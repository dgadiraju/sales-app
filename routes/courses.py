from flask import render_template

from app import app
from app import db
from models.course import Course


@app.route('/courses')
def courses():
    course_recs = db.session.query(Course).all()
    courses = list(map(lambda rec: rec.__dict__, course_recs))
    return render_template('courses.html', courses=courses)