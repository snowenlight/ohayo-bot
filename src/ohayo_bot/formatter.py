from datetime import date


def format_message(
    mta: dict | None,
    weather: dict | None = None,
    weather_error: bool = False,
    pollen: dict | None = None,
    pollen_error: bool = False,
) -> str:
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

    if pollen:
        lines.append("\n【花粉】")
        lines.append(f"木: {pollen['tree_label']}")
        lines.append(f"草: {pollen['grass_label']}")
        lines.append(f"雑草: {pollen['weed_label']}")
    elif pollen_error:
        lines.append("\n【花粉】")
        lines.append("取得失敗")

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
