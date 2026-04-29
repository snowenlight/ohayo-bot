from linebot.v3.messaging import (
    ApiClient,
    Configuration,
    MessagingApi,
    PushMessageRequest,
    TextMessage,
)
from .base import BaseNotifier


class LineNotifier(BaseNotifier):
    def __init__(self, channel_access_token: str, user_id: str):
        config = Configuration(access_token=channel_access_token)
        self._api = MessagingApi(ApiClient(config))
        self._user_id = user_id

    def send(self, message: str) -> None:
        self._api.push_message(
            PushMessageRequest(
                to=self._user_id,
                messages=[TextMessage(type="text", text=message)],
            )
        )
