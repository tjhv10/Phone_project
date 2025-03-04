#!/bin/bash

for i in $(seq 1 30); do
    ip="10.0.0.$i"
    echo "Connecting to $ip..."
    timeout 10s adb connect $ip || echo "Failed to connect to $ip, skipping..."
done

# Usage:
# 1. Connect all devices to the same network
# 2. Run the following commands one after another:
#    chmod +x connect_devices_linux.sh
#    ./connect_devices_linux.sh
# 3. Enjoy!





