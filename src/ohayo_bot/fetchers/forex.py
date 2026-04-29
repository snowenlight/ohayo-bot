import yfinance as yf
from .base import BaseFetcher


class ForexFetcher(BaseFetcher):
    def __init__(self, pairs: list[str]):
        self.pairs = pairs

    def fetch(self) -> dict:
        results = {}
        for pair in self.pairs:
            info = yf.Ticker(pair).fast_info
            results[pair] = {
                "rate": info.last_price,
                "previous_close": info.previous_close,
            }
        return results
