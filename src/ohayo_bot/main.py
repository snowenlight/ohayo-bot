import sys

from .config import (
    LINE_CHANNEL_ACCESS_TOKEN,
    OPENWEATHER_API_KEY,
    POLLEN_LOCATION,
    SLACK_WEBHOOK_URL,
    GOOGLE_POLLEN_API_KEY,
    WEATHER_CITY,
)
from .fetchers.mta import MTAFetcher
from .fetchers.pollen import PollenFetcher
from .fetchers.weather import WeatherFetcher
from .formatter import format_message
from .notifiers.line import LineNotifier
from .notifiers.slack import SlackNotifier


def build_message() -> str:
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

    pollen = None
    pollen_error = False
    if GOOGLE_POLLEN_API_KEY:
        try:
            pollen = PollenFetcher(GOOGLE_POLLEN_API_KEY, POLLEN_LOCATION).fetch()
        except Exception as e:
            print(f"pollen fetch failed: {type(e).__name__}: {e}", file=sys.stderr)
            pollen_error = True

    return format_message(
        mta,
        weather,
        weather_error=weather_error,
        pollen=pollen,
        pollen_error=pollen_error,
    )


def run() -> None:
    message = build_message()
    LineNotifier(LINE_CHANNEL_ACCESS_TOKEN).send(message)
    if SLACK_WEBHOOK_URL:
        SlackNotifier(SLACK_WEBHOOK_URL).send(message)


if __name__ == "__main__":
    run()
