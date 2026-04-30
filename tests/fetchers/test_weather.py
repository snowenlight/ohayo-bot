from unittest.mock import MagicMock, patch

from ohayo_bot.fetchers.weather import WeatherFetcher


@patch("ohayo_bot.fetchers.weather.requests.get")
def test_fetch_returns_weather(mock_get):
    entry = {
        "weather": [{"description": "晴れ"}],
        "main": {"temp": 18.5, "temp_min": 14.0, "temp_max": 22.0},
        "pop": 0.1,
    }
    mock_get.return_value.json.return_value = {"list": [entry] * 8}

    result = WeatherFetcher("fake_key", "Tokyo").fetch()

    assert result["description"] == "晴れ"
    assert result["temp"] == 18.5
    assert result["pop"] == 0.1
