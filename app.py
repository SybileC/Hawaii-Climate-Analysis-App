import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Create an app
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    routes = ['precipitation', 'stations', 'tobs', 'start']
    return routes

@app.route("/precipitation")
def precipitation():
    return






if __name__ == "__main__":
    app.run(debug=True)
