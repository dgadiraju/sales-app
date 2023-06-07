import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

load_dotenv('.env')
db = SQLAlchemy()
app = Flask(__name__)
Bootstrap(app)
host = os.environ.get('SALES_DB_HOST')
port = os.environ.get('SALES_DB_PORT')
db_name = os.environ.get('SALES_DB_NAME')
user = os.environ.get('SALES_DB_USER')
password = os.environ.get('SALES_DB_PASS')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
db.init_app(app)

from routes import users, courses
from models.user import User


@app.route('/')
def hello_world():
    # rec = db.get_or_404(User, 1)
    rec = User.query.get_or_404(1)
    return render_template('index.html', user=rec)
