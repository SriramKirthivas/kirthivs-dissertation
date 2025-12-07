import math

with open('ireland_raw.txt', 'r') as f:
    for line in f:
        parts = line.strip().split('|')
        if len(parts) >= 5:
            ip = parts[3]
            count = int(parts[4])
            # Convert count to CIDR prefix
            prefix = 32 - int(math.log2(count))
            print(f"{ip}/{prefix}")