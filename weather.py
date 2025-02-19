import requests

def get_weather(city):
    API_KEY = "422bf50a11e0a074c03c7636c540e8d6"  # Replace with your actual API key from OpenWeatherMap
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    # Send request to OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display weather information
        print(f"Weather in {city}: {weather_desc.capitalize()}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error: Unable to fetch weather data. Check city name or API key.")

# Get city input from user
city_name = input("Enter city name: ")
get_weather(city_name)
