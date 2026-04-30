import os
from dotenv import load_dotenv

load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN: str = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_USER_ID: str = os.environ["LINE_USER_ID"]
OPENWEATHER_API_KEY: str | None = os.getenv("OPENWEATHER_API_KEY")
WEATHER_CITY: str = os.getenv("WEATHER_CITY", "Tokyo")
STOCK_SYMBOLS: list[str] = (os.getenv("STOCK_SYMBOLS") or "^GSPC,^N225,BTC-USD").split(",")
FOREX_PAIRS: list[str] = (os.getenv("FOREX_PAIRS") or "USDJPY=X,EURJPY=X").split(",")
RATE_SYMBOLS: list[str] = (os.getenv("RATE_SYMBOLS") or "^TNX").split(",")
SLACK_WEBHOOK_URL: str | None = os.getenv("SLACK_WEBHOOK_URL")
