import os
from dotenv import load_dotenv

load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN: str = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
OPENWEATHER_API_KEY: str | None = os.getenv("OPENWEATHER_API_KEY")
WEATHER_CITY: str = os.getenv("WEATHER_CITY", "Tokyo")
GOOGLE_POLLEN_API_KEY: str | None = os.getenv("GOOGLE_POLLEN_API_KEY")
POLLEN_LOCATION: str = os.getenv("POLLEN_LOCATION", "40.7128,-74.0060")
SLACK_WEBHOOK_URL: str | None = os.getenv("SLACK_WEBHOOK_URL")
