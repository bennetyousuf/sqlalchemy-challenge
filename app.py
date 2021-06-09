# Import all dependencies: 
################################################# 

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify 

# Create connection to Hawaii.sqlite file
#################################################

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# # Save references to the measurement and station tables in the database
Measurement = Base.classes.measurement
Station = Base.classes.station

# Initialize Flask
#################################################
app = Flask(__name__)

# Create Flask Routes 
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation (prcp)and date (date) data"""
    
    # Create new variable to store results from query to Measurement table for prcp and date columns
    precipitation_results = session.query(Measurement.prcp, Measurement.date).all()

    # Close session
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
        #1. CREATE AN EMPTY LIST OF all_passengers (WHICH YOU'LL WANT IN DICTIONARY FORM)
        #2. CREATE A FORMAT SAYING FOR THOSE 3 COLUMNS IN VAR "results" (WHICH = YOUR SQLALCHEMY QUERY):
            #CREATE AN EMPTY DICTIONARY CALL passenger_dict: 
            #   "NAME" IN DICT : VALUE NAME FROM VAR results, "AGE":AGE, "SEX":SEX
        #3. APPENND RESULTS FROM passenger_dict 
        #   (AFTER YOU CREATE THE DICT W KEY/VALUE PAIRS) TO EMPTY LIST all_passengers
            # NOTE: BE SURE TO APPEND WITHIN THE FOR LOOP (1 INDENT AFTER FOR) OR ELSE THE VALUES TO APPEND
            #  WONT EXIST 
        # 4. RETURN JSON FORMAT OF all_passengers
    precipitation_results = []
    for prcp, date in precipitation_results:
        precipitation_dict = {}
        precipitation_dict["precipitation"] = prcp
        precipitation_dict["date"] = date
        precipitation_results.append(precipitation_dict)

    return jsonify(precipitation_results) 

if __name__ == '__main__':
    app.run(debug=True) 
