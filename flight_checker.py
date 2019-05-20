from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    try:
        flight_id = request.form.get("flight_id")
    except ValueError:
        return render_template("error.html", error="Invalid flight number")

    # check the flight ID
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", error="No such flight")

    # add passenger
    flight.add_passenger(name)
    return render_template("success.html")


@app.route("/flights")
def flights():
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flight/<int:flight_id>")
def flight(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight.html", flight=flight, passengers=passengers)


if __name__ == '__main__':
    app.run(debug=True)
