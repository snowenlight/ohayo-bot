from datetime import date


def format_message(stocks: dict, forex: dict, weather: dict | None = None, weather_error: bool = False) -> str:
    today = date.today().strftime("%Y年%-m月%-d日")
    lines = [f"おはようございます！ {today}の朝の情報です。\n"]

    if weather:
        lines.append("【天気】")
        lines.append(
            f"{weather['city']}: {weather['description']} "
            f"{weather['temp']:.1f}°C"
            f"（最低{weather['temp_min']:.1f} / 最高{weather['temp_max']:.1f}）"
        )
    elif weather_error:
        lines.append("【天気】")
        lines.append("取得失敗")

    lines.append("\n【マーケット】")
    for pair, data in forex.items():
        name = pair.replace("=X", "")
        lines.append(f"{name}: {data['rate']:.2f}")
    for symbol, data in stocks.items():
        lines.append(f"{symbol}: {data['price']:.2f} {data['currency']}")

    return "\n".join(lines)
