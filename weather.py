import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

print("Change made")

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')
    city = input('Please enter a city name: ')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data = requests.get(request_url, timeout=10).json()

    #pprint(weather_data)
    print(f"\nCurrent Weather for {weather_data['name']}")
    print(f"\nThe temp is {weather_data['main']['temp']}\n")

if __name__ == '__main__':
    get_current_weather()