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
    
    # display routes
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

    # Create session (link) from Python to the DB
    session = Session(engine)
    
    # Calculate date one year from current date
    year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query date and precipitation and filter based on date greater than or equal to year
    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year).all()

    # Close session
    session.close()

    
    precipitation = []
    for date, prcp in data:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['prcp'] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    
    # Create session (link) from Python to the DB
    session = Session(engine)
    
    # Query distinc stations
    stations = session.query(Measurement.station).distinct().all()

    # Close session
    session.close()

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():

    # Create session (link) from Python to the DB
    session = Session(engine)
    
    # Calculate date one year from current date
    year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query station, date and tobs based on station USC00519281 and date greater than year
    station_info = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date > year).all()

    # Close session
    session.close()

    return jsonify(station_info)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start(start=None, end=None):
    
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Select satement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # calculate TMIN, TAVG, TMAX for dates greater than start
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # Unravel results and convert to a list
        temps = list(np.ravel(results))
       
        return jsonify(temps)

    
   # calculate TMIN, TAVG, TMAX for dates between start and end
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    # Unravel results and convert to a list
    temps = list(np.ravel(results))
    
    return jsonify(temps)




if __name__ == "__main__":
    app.run(debug=True)
