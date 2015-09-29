import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from models import Location, Scooter, Watcher
from os import environ

from flask import Flask, jsonify, render_template
# from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
    

engine = create_engine("postgresql://postgres@db_1:5432", echo=True)
make_session = sessionmaker(bind=engine)


@app.route("/hello-world")
def hello():
    return "Hello World!"


@app.route("/")
def index():
    return render_template('index.html', name='foobar', STATIC_BASE=environ['STATIC_BASE'])

@app.route("/v1/scooters")
def get_scooters():
    sesh = make_session()
    return jsonify({
        "object":"list",
        "data":[s.as_dict() for s in sesh.query(Scooter).all()]
    })


@app.route("/v1/locations")
def get_locations():
    sesh = make_session()
    return jsonify({
        "object":"list",
        "data":[s.as_dict() for s in sesh.query(Location).all()]
    })


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)