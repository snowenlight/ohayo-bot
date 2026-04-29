from datetime import date


def _change(current: float, previous: float) -> str:
    pct = (current - previous) / previous * 100
    sign = "+" if pct >= 0 else ""
    return f"({sign}{pct:.1f}%)"


def _change_bp(current: float, previous: float) -> str:
    bp = (current - previous) * 100
    sign = "+" if bp >= 0 else ""
    return f"({sign}{bp:.0f} bp)"


def format_message(stocks: dict, forex: dict, rates: dict, mta: dict | None, weather: dict | None = None, weather_error: bool = False) -> str:
    today = date.today().strftime("%Y年%-m月%-d日")
    lines = [f"おはようございます！ {today}の朝の情報です。\n"]

    if weather:
        lines.append("【天気】")
        lines.append(
            f"{weather['description']} {weather['temp']:.1f}°C"
            f"（最低{weather['temp_min']:.1f} / 最高{weather['temp_max']:.1f}）"
            f" 降水確率{weather['pop'] * 100:.0f}%"
        )
    elif weather_error:
        lines.append("【天気】")
        lines.append("取得失敗")

    lines.append("\n【マーケット】")
    for pair, data in forex.items():
        name = pair.replace("=X", "")
        lines.append(f"{name}: {data['rate']:.2f} {_change(data['rate'], data['previous_close'])}")
    for symbol, data in stocks.items():
        lines.append(f"{symbol}: {data['price']:.2f} {_change(data['price'], data['previous_close'])}")
    for symbol, data in rates.items():
        lines.append(f"{symbol}: {data['price']:.2f}% {_change_bp(data['price'], data['previous_close'])}")

    if mta is not None:
        lines.append("\n【MTA地下鉄】")
        if mta.get("error"):
            lines.append("取得失敗")
        elif mta["disruptions"]:
            for d in mta["disruptions"]:
                lines.append(f"{d['line']}: {d['status']}")
        else:
            lines.append("正常運行")

    return "\n".join(lines)
