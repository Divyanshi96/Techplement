import time
import json
import requests
import argparse
import random


API_KEY = '3263cb6c02664c3490a174204240504'
BASE_URL = f"http://api.weatherapi.com/v1/current.json?"

FAVORITES_FILE = "weather_favorites.json"

def get_weather(city):
  """Fetches weather data for the given city using the weather API."""

  url = f"{BASE_URL}key={API_KEY}&q={city}"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    weather_data = response.json()
    return weather_data
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving weather data for {city}: {e}")
    return None

def display_weather(weather_data):
  """Formats and displays the weather information."""

  if weather_data:
    city = weather_data['location']['name']
    temperature = weather_data['current']['temp_c'] 
    feels_like = weather_data['current']['feelslike_c']
    print(f"City: {city}\nTemperature: {temperature:.1f} °C\nFeels_like: {feels_like}")
  else:
    print("Unable to retrieve weather data.")

def is_valid_city_name(city_name):
  """Checks if the city name is a string with at least 2 characters."""

  return isinstance(city_name, str) and len(city_name) >= 2

def load_favorites():
  """Loads favorite cities from the JSON file (if it exists)."""

  try:
    with open(FAVORITES_FILE, 'r') as f:
      return json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    return []

def save_favorites(favorites):
  """Saves favorite cities to the JSON file."""

  with open(FAVORITES_FILE, 'w') as f:
    json.dump(favorites, f, indent=2)

def add_favorite(city):
  """Adds a city to the favorites list, validating city name and avoiding duplicates."""

  if not is_valid_city_name(city):
    print("Invalid city name. Please enter a string with at least 2 characters.")
    return

  favorites = load_favorites()
  if city not in favorites:
    favorites.append(city)
    save_favorites(favorites)
    print(f"City '{city}' added to favorites.")
  else:
    print(f"City '{city}' already exists in favorites.")

def remove_favorite(city):
  """Removes a city from the favorites list, validating city name and existence."""

  if not is_valid_city_name(city):
    print("Invalid city name. Please enter a string with at least 2 characters.")
    return

  favorites = load_favorites()
  if city in favorites:
    favorites.remove(city)
    save_favorites(favorites)
    print(f"City '{city}' removed from favorites.")
  else:
    print(f"City '{city}' not found in favorites.")

def list_favorites():
  """Prints the list of favorite cities."""

  favorites = load_favorites()
  if not favorites:
    print("No favorite cities yet.")
  else:
    print("Your favorite cities:")
    return favorites

def main():

  parser = argparse.ArgumentParser(description="Weather Checking Application")
  parser.add_argument("city", nargs="?", help="City name to check weather (optional)")
  parser.add_argument("-f", "--favorite", action="store_true", help="View or manage favorite cities")
  parser.add_argument("-r", "--refresh", action="store_true", help="Enable auto-refresh every 15-30 seconds")
  args = parser.parse_args()
  if args.city:
    weather_data = get_weather(args.city)
    display_weather(weather_data)
    if args.refresh:
       city_to_check = args.city
       print(f"Auto-refresh enabled for {city_to_check} (refreshing every 15-30 seconds)")
       while True:
           time.sleep(random.randint(15, 30))
           weather_data = get_weather(city_to_check)
           display_weather(weather_data)
  elif args.favorite:
    print("Favorite Cities Management:")
    while True:
        action = input("Enter 'a' to add, 'd' to delete, 'r' to read favorite city weather or 'q' to quit: ").lower()
        if action == 'q':
            break
        elif action == 'a':
            city = input("Enter the city name to add: ")
            add_favorite(city)
        elif action == 'r':
            favorites = list_favorites()
            for city in favorites:
              weather_data = get_weather(city)
              display_weather(weather_data)
        elif action == 'd':
            city = input("Enter the city name to remove: ")
            remove_favorite(city)
        else:
            print("Invalid action. Please enter 'a', 'r', or 'q'.")

if __name__ == "__main__":
  main()
