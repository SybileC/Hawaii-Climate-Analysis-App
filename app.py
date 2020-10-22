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
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > 2016-8-23).all()

    session.close()

    precipitation = []
    for date, prcp in data:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['prcp'] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation_dict)


@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    
    stations = session.query(Measurement.station).distinct().all()

    session.close()

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)
    
    station_info = session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date > 2016-8-23).all()

    session.close()

    return jsonify(station_info)


if __name__ == "__main__":
    app.run(debug=True)
