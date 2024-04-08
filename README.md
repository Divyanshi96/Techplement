Weather Checking Application


This Python script provides a user-friendly weather checking application with features for:

Checking weather for a specific city.
Managing a list of favorite cities for quick weather checks.
Setting up auto-refresh for continuous updates on a specific city's weather.

How to Use

Save the code: Save the script as a Python file (e.g., weather_checker.py).
Replace API Key: Create an account on weather API using this url = "https://www.weatherapi.com/" and now you'll have your API key
Run the script: Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using python weather_checker.py (or python3 depending on your Python version).

Command-Line Arguments

The script supports the following command-line arguments:

city (optional): The name of the city to check the weather for.
-f or --favorite: Opens the favorite city management menu.
-r or --refresh: Enables auto-refresh for the provided city weather (updates every 15-30 seconds).

Examples

Get weather for London: python weather_checker.py London
Manage favorite cities: python weather_checker.py -f
Get weather for New York with auto-refresh: python weather_checker.py New York -r

Requirements

Python 3 (tested with 3.x versions)
requests library: You can install it using pip install requests
