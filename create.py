import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'  # os.getenv("sqlite:////tmp/test.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def insert():
    flight = Flight(origin="New York", destination="Tashkent", duration=900)
    db.session.add(flight)
    flight = Flight(origin="London", destination="Moscow", duration=450)
    db.session.add(flight)
    db.session.commit()


def delete():
    flights = Flight.query.all()
    for flight in flights:
        db.session.delete(flight)
    db.session.commit()


def main():
    db.create_all()


def print_all():
    for f in Flight.query.all():
        print(f"{f.origin} to {f.destination}")


if __name__ == "__main__":
    with app.app_context():
        print_all()
