import requests

API_KEY = "8d5b805268b1ac1a127e1422cbd851a6"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data.get("cod") != 200:
        print("City not found!")
        return

    print("\nWeather Report")
    print("---------------------")
    print("City:", city)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"])

city = input("Enter City Name: ")

get_weather(city)