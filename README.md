# Hawaii-Climate-Analysis-App

- Designed a Flask API based on the queries developed in climate_starter.ipynb file
    - Home Page (/)
        - Displaying all of the available routes
        ![Home Page](Images/Home_page.PNG)
    
    - Precipitation Page (/api/v1.0/precipitation)
        - Displaying the last 12 months of precipitation data
        ![Precipitation Page](Images/Precipitation_page.PNG)

    - Sations Page (/api/v1.0/stations)
        - Displaying a JSON list of stations from the dataset
        ![Stations Page](Images/Stations_page.PNG)

    - Temperature Observations Page (/api/v1.0/tobs)
        - Displaying the dates and temperature observations of the most active station for the last year of data
        ![TOBS Page](Images/tobs_page.PNG)

    - Calculation Page (/api/v1.0/<start>/<end>)
        - Displaying a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range
        ![Calculation Page](Images/Calculation_page.PNG)