import json
import requests
import os

def load_destinations():
    """Load travel destinations from JSON file."""
    with open("data/destinations.json", "r", encoding="utf-8") as file:
        return json.load(file)


API_KEY = "1a7ccb332e29c111e6fa0bbbb2d24fe9"  # Set this in your system environment variables
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch real-time weather data for a given city using OpenWeather API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)  # ✅ Added timeout
        response.raise_for_status()  # ✅ Raise an error for bad responses
        data = response.json()

        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        return f"The weather in {city} is {temp}°C with {weather_desc}."

    except requests.exceptions.RequestException:
        return f"⚠️ Unable to fetch real-time weather for {city}. Try again later."
