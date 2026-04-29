import requests
from .base import BaseFetcher

_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


class WeatherFetcher(BaseFetcher):
    def __init__(self, api_key: str, city: str):
        self.api_key = api_key
        self.city = city

    def fetch(self) -> dict:
        resp = requests.get(
            _BASE_URL,
            params={
                "q": self.city,
                "appid": self.api_key,
                "units": "metric",
                "lang": "ja",
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        return {
            "city": self.city,
            "description": data["weather"][0]["description"],
            "temp": data["main"]["temp"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
        }
