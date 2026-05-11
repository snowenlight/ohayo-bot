import requests
from .base import BaseFetcher

_BASE_URL = "https://api.tomorrow.io/v4/weather/forecast"

# Tomorrow.io 花粉指数 (0-5) のラベル
_LEVELS = ["なし", "極低", "低", "中", "高", "極高"]


def _label(value: int | float | None) -> str:
    if value is None:
        return "不明"
    idx = max(0, min(5, int(round(value))))
    return _LEVELS[idx]


class PollenFetcher(BaseFetcher):
    def __init__(self, api_key: str, location: str):
        self.api_key = api_key
        self.location = location

    def fetch(self) -> dict:
        resp = requests.get(
            _BASE_URL,
            params={
                "location": self.location,
                "fields": "treeIndex,grassIndex,weedIndex",
                "timesteps": "1h",
                "apikey": self.api_key,
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        values = data["timelines"]["hourly"][0]["values"]
        return {
            "tree": values.get("treeIndex"),
            "grass": values.get("grassIndex"),
            "weed": values.get("weedIndex"),
            "tree_label": _label(values.get("treeIndex")),
            "grass_label": _label(values.get("grassIndex")),
            "weed_label": _label(values.get("weedIndex")),
        }
