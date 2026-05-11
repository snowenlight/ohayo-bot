from unittest.mock import patch

from ohayo_bot.fetchers.pollen import PollenFetcher


@patch("ohayo_bot.fetchers.pollen.requests.get")
def test_fetch_returns_pollen(mock_get):
    mock_get.return_value.json.return_value = {
        "dailyInfo": [
            {
                "pollenTypeInfo": [
                    {
                        "code": "TREE",
                        "indexInfo": {"value": 1, "category": "Very Low"},
                    },
                    {
                        "code": "GRASS",
                        "indexInfo": {"value": 3, "category": "Moderate"},
                    },
                    {"code": "WEED"},
                ]
            }
        ]
    }

    result = PollenFetcher("fake_key", "40.7128,-74.0060").fetch()

    assert result["tree"] == {"value": 1, "label": "極低"}
    assert result["grass"] == {"value": 3, "label": "中"}
    assert result["weed"] == {"value": None, "label": "データなし"}


@patch("ohayo_bot.fetchers.pollen.requests.get")
def test_fetch_handles_missing_type(mock_get):
    mock_get.return_value.json.return_value = {
        "dailyInfo": [{"pollenTypeInfo": []}]
    }

    result = PollenFetcher("fake_key", "40.7128,-74.0060").fetch()

    assert result["tree"]["label"] == "データなし"
    assert result["grass"]["label"] == "データなし"
    assert result["weed"]["label"] == "データなし"
