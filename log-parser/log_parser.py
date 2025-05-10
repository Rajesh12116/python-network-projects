with open("router_logs.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    if "changed state to down" in line:
        print(f" Interface down alert: {line.strip()}")