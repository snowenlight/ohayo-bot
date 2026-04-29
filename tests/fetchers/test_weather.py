from unittest.mock import MagicMock, patch

from ohayo_bot.fetchers.weather import WeatherFetcher


@patch("ohayo_bot.fetchers.weather.requests.get")
def test_fetch_returns_weather(mock_get):
    mock_get.return_value.json.return_value = {
        "weather": [{"description": "晴れ"}],
        "main": {"temp": 18.5, "temp_min": 14.0, "temp_max": 22.0},
    }

    result = WeatherFetcher("fake_key", "Tokyo").fetch()

    assert result["city"] == "Tokyo"
    assert result["description"] == "晴れ"
    assert result["temp"] == 18.5
