import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create an app
app = Flask(__name__)


@app.route("/")
def home():
    
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():

    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > year).all()

    session.close()

    precipitation = []
    for prcp in results:
        precipitation_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        precipitation.append(precipitation_dict)

    return jsonify(precipitation_dict)









if __name__ == "__main__":
    app.run(debug=True)
