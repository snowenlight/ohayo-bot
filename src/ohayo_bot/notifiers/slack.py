import requests
from .base import BaseNotifier


class SlackNotifier(BaseNotifier):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send(self, message: str) -> None:
        resp = requests.post(
            self.webhook_url,
            json={"text": message},
            timeout=10,
        )
        resp.raise_for_status()
