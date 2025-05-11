import socket

# Target IP address (change if needed)
target_ip = "8.8.8.8"

# Range of ports to scan
start_port = 20
end_port = 100

print(f"🔍 Scanning {target_ip} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # Set timeout to half a second

    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"✅ Port {port} is open")
    else:
        print(f"❌ Port {port} is closed")

    sock.close()