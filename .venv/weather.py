from dotenv import load_dotenv
from pprint import pprint
import requests
import os 

load_dotenv()

def get_current_weather(city="Bursa city"):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={os.getenv('API_KEY')}"

    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n ***GET CURRENT WEATHER CONDİTİONS*** \n")

    city= input("\n Plase enter a city name: \n")


    # check for empty strings or string with only spaces
    if not bool(city.strip()):
        city ="Bursa"
    
    weather_data = get_current_weather(city)

    print("\n ")
    pprint(weather_data)