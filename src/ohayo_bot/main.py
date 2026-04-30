from .config import (
    FOREX_PAIRS,
    LINE_CHANNEL_ACCESS_TOKEN,
    OPENWEATHER_API_KEY,
    RATE_SYMBOLS,
    SLACK_WEBHOOK_URL,
    STOCK_SYMBOLS,
    WEATHER_CITY,
)
from .fetchers.forex import ForexFetcher
from .fetchers.mta import MTAFetcher
from .fetchers.stock import StockFetcher
from .fetchers.weather import WeatherFetcher
from .formatter import format_message
from .notifiers.line import LineNotifier
from .notifiers.slack import SlackNotifier


def build_message() -> str:
    stocks = StockFetcher(STOCK_SYMBOLS).fetch()
    forex = ForexFetcher(FOREX_PAIRS).fetch()
    rates = StockFetcher(RATE_SYMBOLS).fetch()

    try:
        mta = MTAFetcher().fetch()
    except Exception:
        mta = {"disruptions": [], "error": True}

    weather = None
    weather_error = False
    if OPENWEATHER_API_KEY:
        try:
            weather = WeatherFetcher(OPENWEATHER_API_KEY, WEATHER_CITY).fetch()
        except Exception:
            weather_error = True

    return format_message(stocks, forex, rates, mta, weather, weather_error=weather_error)


def run() -> None:
    message = build_message()
    LineNotifier(LINE_CHANNEL_ACCESS_TOKEN).send(message)
    if SLACK_WEBHOOK_URL:
        SlackNotifier(SLACK_WEBHOOK_URL).send(message)


if __name__ == "__main__":
    run()
