def get_suggestions(data):
    suggestions = []

    if data["cpu"] > 80:
        suggestions.append("Close background applications")

    if data["ram"] > 80:
        suggestions.append("Reduce memory usage")

    if data["disk"] > 80:
        suggestions.append("Free disk space")

    if not suggestions:
        suggestions.append("System is running smoothly")

    return suggestions