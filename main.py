from flask import Flask, jsonify
from flask_cors import CORS
import csv
import os

app = Flask(__name__)


# @app.route('/')
# def index():
#     return jsonify({"this is where my flask app would go": "IF I HAD ONE 🚅"})

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)


@app.route("/")
def welcome():
    """May Wildlife Sample Data."""
    return (
        f"Available Routes:<br/>"
        f"/api/patients<br/>"
        f"/api/statuscodes<br/>"
        f"/api/animals<br/>"
        f"/api/locations<br/>"
    )


@app.route("/api/patients")
def patients():
    with open('resources/Patients.csv') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            # Convert integer values to int
            row['stay_length'] = int(row['stay_length'])
            data.append(row)
    return jsonify(data)


@app.route("/api/statuscodes")
def statuscodes():
    with open('resources/StatusCodes.csv') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            # Convert integer values to int
            row['status_count'] = int(row['status_count'])
            data.append(row)
    return jsonify(data)


@app.route("/api/animals")
def animals():
    with open('resources/Animals.csv') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            # Convert integer values to int
            row['species_count'] = int(row['species_count'])
            data.append(row)
    return jsonify(data)

@app.route("/api/locations")
def locations():
    with open('resources/Places.csv') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5001))
