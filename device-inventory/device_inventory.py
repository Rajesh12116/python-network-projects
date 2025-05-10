# device_inventory.py
devices = [
    {
        "hostname": "Router1",
        "ip": "192.168.1.1",
        "vendor": "Cisco",
        "location": "Data Center 1"
    },
    {
        "hostname": "Switch1",
        "ip": "192.168.1.2",
        "vendor": "Juniper",
        "location": "Branch Office"
    },
    {
        "hostname": "Firewall1",
        "ip": "192.168.1.3",
        "vendor": "Palo Alto",
        "location": "HQ"
    }
]
# Display all devices
print("Network Device Inventory:")
print("-" * 40)
for device in devices:
    print(f"{device['hostname']} | {device['ip']} | {device['vendor']} | {device['location']}")