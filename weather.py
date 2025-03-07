import requests
import argparse

API_KEY = "08801942f872442f94bdbfd63329da27"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"Weather in {city}:")
    print(f"  Condition: {weather}")
    print(f"  Temperature: {temperature}°C")
    print(f"  Humidity: {humidity}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get weather for a city")
    parser.add_argument("--city", required=True, help="City name")
    args = parser.parse_args()

    get_weather(args.city)
