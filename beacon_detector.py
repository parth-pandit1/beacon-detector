import statistics

flows = {
    "192.168.1.5:evil-c2.com:443": [0, 60.1, 120.3, 180.2, 240.1, 300.4],
    "192.168.1.5:google.com:443":  [0, 5.2, 18.7, 45.1, 102.3, 200.8],
    "192.168.1.5:update.microsoft.com:80": [0, 3600.1, 7200.3, 10800.2],
}

print(f"{'Flow':<35} {'Mean':>8} {'CV':>8} {'Status'}")
print("-" * 65)

for flow, timestamps in flows.items():
    if len(timestamps) < 3:
        continue
    intervals = [timestamps[i]-timestamps[i-1]
                 for i in range(1, len(timestamps))]
    mean = statistics.mean(intervals)
    std = statistics.stdev(intervals)
    cv = std / mean
    status = "BEACON!" if cv < 0.1 else "Normal"
    print(f"{flow:<35} {mean:>8.1f}s {cv:>8.4f} {status}")