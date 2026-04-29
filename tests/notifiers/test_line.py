from unittest.mock import MagicMock, patch

from ohayo_bot.notifiers.line import LineNotifier


@patch("ohayo_bot.notifiers.line.MessagingApi")
@patch("ohayo_bot.notifiers.line.ApiClient")
def test_send_calls_push_message(mock_client, mock_api_class):
    mock_api = MagicMock()
    mock_api_class.return_value = mock_api

    notifier = LineNotifier("token", "user123")
    notifier.send("おはよう")

    mock_api.push_message.assert_called_once()
