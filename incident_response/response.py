
blocked_ips = []

def block_ip(ip):
    if ip not in blocked_ips:
        blocked_ips.append(ip)
        return f"IP {ip} blocked"
    return "IP already blocked"
