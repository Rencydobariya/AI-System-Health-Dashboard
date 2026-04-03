def calculate_trust_score(data):
    score = 100

    if data["cpu"] > 80:
        score -= 10
    if data["ram"] > 80:
        score -= 10
    if data["disk"] > 80:
        score -= 15

    return max(score, 0)