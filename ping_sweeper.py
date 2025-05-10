import os

# Read IPs from file
with open("ip_list.txt", "r") as file:
    ips = [line.strip() for line in file.readlines()]

# Loop through each IP and ping it
for ip in ips:
    print(f"Pinging {ip}...")
    
    # If you're on Windows, use 'ping -n 2'
    response = os.system(f"ping -n 2 {ip} > nul")  # for Windows
    # For Linux/macOS: use 'ping -c 2 {ip} > /dev/null'

    if response == 0:
        print(f"✅ {ip} is reachable.\n")
    else:
        print(f"❌ {ip} is unreachable.\n")