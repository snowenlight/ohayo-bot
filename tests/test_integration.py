"""
統合テスト: 実際にAPIを叩いてデータ取得〜フォーマットまでを検証する。
実行: pytest tests/test_integration.py -v -s
"""
import pytest
from ohayo_bot.main import build_message


def test_build_message():
    message = build_message()

    print("\n--- 生成メッセージ ---")
    print(message)
    print("---------------------")

    assert "おはようございます" in message
    assert "【マーケット】" in message
    assert "【MTA地下鉄】" in message
