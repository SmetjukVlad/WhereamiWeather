from datetime import datetime
from enum import Enum
from typing import NamedTuple

from .coordinates import Coordinates

Celsius = int

class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG =  "Туман"
    CLOUDS = "Облачно"

class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset:datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    """REQUEST WEATHER IN OpenWeather API and returns it"""
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-05 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-05 23:00:00"),
        city="Minsk"
    )