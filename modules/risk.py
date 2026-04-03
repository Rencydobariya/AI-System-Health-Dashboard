def calculate_risk(data):
    risk = (data["cpu"] + data["ram"] + data["disk"]) / 3
    trust = 100 - risk
    return int(risk), int(trust)


def get_suggestion(data):
    if data["cpu"] > 80:
        return "🔥 CPU High! Close heavy apps."
    elif data["ram"] > 80:
        return "⚡ RAM High! Restart or close apps."
    elif data["disk"] > 85:
        return "💽 Disk Almost Full! Clean storage."
    else:
        return "✅ System is healthy!"