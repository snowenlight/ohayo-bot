from .config import (
    FOREX_PAIRS,
    LINE_CHANNEL_ACCESS_TOKEN,
    LINE_USER_ID,
    OPENWEATHER_API_KEY,
    STOCK_SYMBOLS,
    WEATHER_CITY,
)
from .fetchers.forex import ForexFetcher
from .fetchers.stock import StockFetcher
from .fetchers.weather import WeatherFetcher
from .formatter import format_message
from .notifiers.line import LineNotifier


def run() -> None:
    stocks = StockFetcher(STOCK_SYMBOLS).fetch()
    forex = ForexFetcher(FOREX_PAIRS).fetch()
    weather = None
    weather_error = False
    if OPENWEATHER_API_KEY:
        try:
            weather = WeatherFetcher(OPENWEATHER_API_KEY, WEATHER_CITY).fetch()
        except Exception:
            weather_error = True

    message = format_message(stocks, forex, weather, weather_error=weather_error)

    LineNotifier(LINE_CHANNEL_ACCESS_TOKEN, LINE_USER_ID).send(message)


if __name__ == "__main__":
    run()
