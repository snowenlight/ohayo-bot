import requests
from .base import BaseFetcher

_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


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
                "cnt": 8,  # 直近24時間（3時間×8）
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        entries = data["list"]
        return {
            "description": entries[0]["weather"][0]["description"],
            "temp": entries[0]["main"]["temp"],
            "temp_min": min(e["main"]["temp_min"] for e in entries),
            "temp_max": max(e["main"]["temp_max"] for e in entries),
            "pop": max(e.get("pop", 0) for e in entries),
        }
