import sys
from dataclasses import dataclass
import requests


# można by też uzyć namedtuple z collections

@dataclass
class Weather:
    name: str
    temp: float
    humidity: float
    air_pressure: float

    def raport(self):
        return f"""Pogoda w {self.name}:
temperatura: {self.temp}
wilgotność: {self.humidity}
ciśnienie: {self.air_pressure}
"""


def get_location_id(location_name):
    query_url = "https://www.metaweather.com/api/location/search/?query=" + location_name
    resp = requests.get(query_url)
    return resp.json()[0]["woeid"]


def get_location_weather(location_id):
    query_url = f"https://www.metaweather.com/api/location/{location_id}/"
    resp = requests.get(query_url)
    location_name = resp.json()['title']
    data = resp.json()['consolidated_weather'][0]
    weather = Weather(
        name=location_name,
        temp=data["the_temp"],
        humidity=data["humidity"],
        air_pressure=data["air_pressure"]
    )
    return weather

if __name__ == "__main__":
    print(sys.argv)
    location_name = sys.argv[1] if len(sys.argv) == 2 else "warsaw"
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    print(weather.raport())



# def print_weather(resp):
#     print(f"Pogoda dla miasta {miasto}:")
#     for weather in resp.json()['consolidated_weather']:
#         print(f"Data: {weather['applicable_date']}")
#         print(
#             f"\tPogoda: {weather['weather_state_name']}, "
#             f"srednia-temp: {round(weather['the_temp'], 1)}, "
#             f"wiatr: {round(weather['wind_speed'], 1)} km/h, "
#             f"cisnienie powietrza: {round(weather['air_pressure'], 1)} hPa")
#print_weather(get_location_weather(get_location_id(miasto)))


