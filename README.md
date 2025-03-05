# Geocoding Utility

This utility retrieves location information using the OpenWeatherMap Geocoding API for US locations.

## Requirements

- Python 3.6+
- requests library

## Installation

1. Clone this repository
2. Install the required library:


## Usage

Run the utility from the command line:
```
python geoloc_util.py "Madison, WI" "12345" "Chicago, IL" "10001"
```
You can provide multiple locations as arguments, including city/state combinations and zip codes.

## Running Tests

To run the integration tests:
```
python -m unittest test_geoloc_util.py
```

## API Key

The utility uses a provided API key. If you need to change it, update the `API_KEY` variable in `geoloc_util.py`.
