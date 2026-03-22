import os
import requests
from dotenv import load_dotenv
#from google.colab import userdata

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    # NOTE: Do NOT log user location data.
    # Logging city names can violate privacy principles such as GDPR (data minimization),
    # since location data can be considered personal/sensitive information.

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        #Task 2 — Handle rate limiting & errors
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            print(f"Temperature: {temp}°C, Condition: {weather}")

        elif response.status_code == 429:
            print("Too many requests. Please wait a moment and try again.")

        elif response.status_code == 401:
            print("Invalid API key. Check your configuration.")

        elif response.status_code == 404:
            print("City not found. Please enter a valid city name.")

        else:
            print(f"Unexpected error: {response.status_code}")

    except requests.exceptions.RequestException:
        print(" Network error. Please check your internet connection.")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)