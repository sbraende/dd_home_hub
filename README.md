# Climate Monitoring Dashboard

This project is a climate monitoring dashboard that displays temperature and humidity data from different sources in real-time. It uses the Dash framework for creating the web interface and SQLite for data storage.

## Project Structure

- `app.py`: The main script that initializes and runs the climate monitoring server.
- `config.json`: Configuration file containing settings for the interior and exterior climate sources and the web server.
- `dashboard.py`: The script that defines the web dashboard using Dash.
- `database.py`: Handles database connections and data storage.
- `exterior_climate.py`: Collects data from an external weather API (OpenWeather).
- `interior_climate.py`: Collects data from multiple Raspberry Pi devices on an internal network.
- `utilities.py`: Contains utility functions for working with JSON configuration files and temperature units conversion.

## Installation

1. Clone the repository:
``` shell 
https://github.com/sbraende/dd_home_hub.git
```


2. Install the required Python packages:
```
pip install dash
sudo apt-get install python3-pandas
pip3 install --upgrade bottleneck
pip3 install --upgrade numexpr
```

3. Rename `config_template.json` to `config.json`. Type your  specific configuration settings, such as API keys and device addresses.

## Usage

1. Start the climate monitoring server:
``` shell 
python3 app.py 
```


2. Access the dashboard by opening a web browser and navigating to `http://localhost:8050`. You can specify a different host and port in the `config.json` file.

3. The dashboard will display real-time temperature and humidity data from the configured sources.

## Dashboard Structure

The dashboard consists of a line chart that displays temperature data over time. It periodically updates the data every 10 seconds.


