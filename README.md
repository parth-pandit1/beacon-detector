# C2 Beacon Detector 

A Python tool that detects Command-and-Control (C2) beacon traffic 
by analyzing inter-packet timing regularity using Coefficient of Variation (CV).

## How it works
Malware beacons check in with C2 servers at regular intervals.
Humans never browse that regularly — machines do!

CV = Standard Deviation / Mean
- CV < 0.1 = 🚨 BEACON CANDIDATE
- CV > 0.1 = ✅ Normal traffic

## Usage
```bash
python3 beacon_detector.py
``
## Skills Demonstrated
- Network traffic analysis
- C2 beacon detection
- Statistical analysis (CV scoring)
- Python scripting

#CyberSecurity #MalwareAnalysis #NetworkForensics
