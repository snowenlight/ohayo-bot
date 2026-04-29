from unittest.mock import MagicMock, patch

from ohayo_bot.fetchers.forex import ForexFetcher


@patch("ohayo_bot.fetchers.forex.yf.Ticker")
def test_fetch_returns_rate(mock_ticker):
    mock_info = MagicMock()
    mock_info.last_price = 150.25
    mock_ticker.return_value.fast_info = mock_info

    result = ForexFetcher(["USDJPY=X"]).fetch()

    assert result["USDJPY=X"]["rate"] == 150.25
