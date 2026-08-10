from dotenv import load_dotenv
import os
import requests
import sys

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Unable to fetch weather')}")
        return

    print(f"\nWeather in {data['name']}, {data['sys']['country']}")
    print(f"🌡 Temperature: {data['main']['temp']}°C")
    print(f"💨 Wind: {data['wind']['speed']} m/s")
    print(f"☁️ Condition: {data['weather'][0]['description'].capitalize()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
    else:
        city = " ".join(sys.argv[1:])
        get_weather(city)