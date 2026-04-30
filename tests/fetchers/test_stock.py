from unittest.mock import MagicMock, patch

from ohayo_bot.fetchers.stock import StockFetcher


@patch("ohayo_bot.fetchers.stock.yf.Ticker")
def test_fetch_returns_price(mock_ticker):
    mock_info = MagicMock()
    mock_info.last_price = 2500.0
    mock_info.currency = "JPY"
    mock_ticker.return_value.fast_info = mock_info

    result = StockFetcher(["7203.T"]).fetch()

    assert result["7203.T"]["price"] == 2500.0
    assert result["7203.T"]["previous_close"] is not None
