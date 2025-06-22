# tools/port_scanner.py

import socket

def scan_ports(target, ports):
    print(f"\n[🔍] Scanning {target}...\n")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 8080]
    scan_ports(target, common_ports)
