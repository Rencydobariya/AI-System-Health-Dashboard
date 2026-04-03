def simple_ai(user_input, system_data):
    msg = user_input.lower()

    cpu = system_data["cpu"]
    ram = system_data["ram"]
    disk = system_data["disk"]

    # Greetings
    if "hi" in msg or "hello" in msg:
        return "👋 Hello! I am your System AI Assistant. Ask me about your system!"

    elif "bye" in msg:
        return "👋 Goodbye! Stay safe and keep your system healthy."

    # System Questions
    elif "cpu" in msg:
        return f"🧠 CPU Usage is {cpu}%. Keep it below 80% for best performance."

    elif "ram" in msg:
        return f"💾 RAM Usage is {ram}%. Try closing apps if above 80%."

    elif "disk" in msg:
        return f"💽 Disk Usage is {disk}%. Clean storage if above 85%."

    elif "performance" in msg or "health" in msg:
        if cpu > 80 or ram > 80:
            return "⚠️ System performance is LOW. Close background apps."
        else:
            return "✅ System is running smoothly."

    # Default intelligent reply
    else:
        return "🤖 I can help with system performance, CPU, RAM, Disk and safety tips!"