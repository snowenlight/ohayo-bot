import yfinance as yf
from .base import BaseFetcher


class StockFetcher(BaseFetcher):
    def __init__(self, symbols: list[str]):
        self.symbols = symbols

    def fetch(self) -> dict:
        results = {}
        for symbol in self.symbols:
            info = yf.Ticker(symbol).fast_info
            results[symbol] = {
                "price": info.last_price,
                "previous_close": info.previous_close,
            }
        return results
