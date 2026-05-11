from unittest.mock import patch

from ohayo_bot.fetchers.pollen import PollenFetcher


@patch("ohayo_bot.fetchers.pollen.requests.get")
def test_fetch_returns_pollen(mock_get):
    mock_get.return_value.json.return_value = {
        "timelines": {
            "hourly": [
                {"values": {"treeIndex": 3, "grassIndex": 1, "weedIndex": 0}},
            ]
        }
    }

    result = PollenFetcher("fake_key", "40.7,-74.0").fetch()

    assert result["tree"] == 3
    assert result["grass"] == 1
    assert result["weed"] == 0
    assert result["tree_label"] == "中"
    assert result["grass_label"] == "極低"
    assert result["weed_label"] == "なし"


@patch("ohayo_bot.fetchers.pollen.requests.get")
def test_fetch_handles_missing_values(mock_get):
    mock_get.return_value.json.return_value = {
        "timelines": {"hourly": [{"values": {}}]}
    }

    result = PollenFetcher("fake_key", "40.7,-74.0").fetch()

    assert result["tree"] is None
    assert result["tree_label"] == "不明"
