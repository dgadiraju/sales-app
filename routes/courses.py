from flask import render_template, request

from app import app
from app import db
from models.course import Course


@app.route('/courses')
def courses():
    course_recs = db.session.query(Course).all()
    courses = list(map(lambda rec: rec.__dict__, course_recs))
    return render_template('courses.html', courses=courses)


@app.route('/course', methods=['GET'])
def course():
    course_id = request.args.get('course_id')
    course = Course.query.get(course_id)
    return render_template('course_detail.html', course=course)
