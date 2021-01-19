import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

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
    
    year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year).all()

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
    
    year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    station_info = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date > year).all()

    session.close()

    return jsonify(station_info)


# @app.route("/api/v1.0/<start>")
# def start(start):


    


# @app.route("/api/v1.0/<start>/<end>")
# def start_end(start, end):



if __name__ == "__main__":
    app.run(debug=True)
