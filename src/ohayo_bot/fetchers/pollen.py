import requests
from .base import BaseFetcher

_BASE_URL = "https://pollen.googleapis.com/v1/forecast:lookup"

_CATEGORY_JA = {
    "None": "なし",
    "Very Low": "極低",
    "Low": "低",
    "Moderate": "中",
    "High": "高",
    "Very High": "極高",
}


class PollenFetcher(BaseFetcher):
    def __init__(self, api_key: str, location: str):
        self.api_key = api_key
        lat, lon = location.split(",")
        self.lat = float(lat)
        self.lon = float(lon)

    def fetch(self) -> dict:
        resp = requests.get(
            _BASE_URL,
            params={
                "key": self.api_key,
                "location.latitude": self.lat,
                "location.longitude": self.lon,
                "days": 1,
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        types = data["dailyInfo"][0].get("pollenTypeInfo", [])
        by_code = {t["code"]: t for t in types}

        return {
            "tree": _entry(by_code.get("TREE")),
            "grass": _entry(by_code.get("GRASS")),
            "weed": _entry(by_code.get("WEED")),
        }


def _entry(info: dict | None) -> dict:
    if not info or "indexInfo" not in info:
        return {"value": None, "label": "データなし"}
    idx = info["indexInfo"]
    return {
        "value": idx.get("value"),
        "label": _CATEGORY_JA.get(idx.get("category", ""), idx.get("category", "不明")),
    }
