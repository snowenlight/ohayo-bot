from linebot.v3.messaging import (
    ApiClient,
    BroadcastRequest,
    Configuration,
    MessagingApi,
    TextMessage,
)
from .base import BaseNotifier


class LineNotifier(BaseNotifier):
    def __init__(self, channel_access_token: str):
        config = Configuration(access_token=channel_access_token)
        self._api = MessagingApi(ApiClient(config))

    def send(self, message: str) -> None:
        self._api.broadcast(
            BroadcastRequest(
                messages=[TextMessage(type="text", text=message)],
            )
        )
