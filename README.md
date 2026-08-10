# Weather CLI 
A simple command‑line tool that fetches real‑time weather data using the OpenWeatherMap API.
Built in Python, this script lets you quickly check the temperature, humidity, and general conditions for any city.

Features
Fetches live weather data from OpenWeatherMap

Displays temperature, humidity, and weather description

Graceful error handling for invalid cities

Secure API key loading using ``` .env ```

Lightweight and easy to run

## Requirements
Python 3.10+

``` requests ```

``` python-dotenv ```

Install dependencies with:
``` pip install -r requirements.txt ```

## Setup

### 1. Clone the repository

``` bash
git clone https://github.com/wisalhab/weather-cli.git
cd weather-cli
```

### 2. Create your ``` .env ``` file
Inside the project folder, create a file named ``` .env ``` :

``` Code
API_KEY=your_openweathermap_api_key_here
```

This file is not tracked by Git and stays private.

## Usage
Run the script with a city name:
```Bash
python weather.py Beirut
```
Example output: 
``` Code
Temperature: 30°C
Humidity: 65%
Weather: Clear sky
```

## Project Structure
```
weather-cli/
│
├── weather.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Notes 
Your API key must be valid for the script to work.

``` .env ``` is intentionally excluded from GitHub for security.

Anyone cloning your repo must create their own ``` .env ``` file.

