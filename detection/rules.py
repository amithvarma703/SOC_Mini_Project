
def detect_bruteforce(logs):
    ip_count = {}
    alerts = []

    for log in logs:
        if "FAILED_LOGIN" in log:
            ip = log.split("ip=")[1].strip()
            ip_count[ip] = ip_count.get(ip, 0) + 1

            if ip_count[ip] == 3:
                alerts.append({
                    "type": "Brute Force Attack",
                    "ip": ip,
                    "severity": "High"
                })
    return alerts
