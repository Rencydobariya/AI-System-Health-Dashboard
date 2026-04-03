import psutil

def get_system_data():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }