#!/bin/bash

for i in $(seq 40 70); do
    ip="10.0.0.$i"
    echo "Connecting to $ip..."
    adb connect $ip
done

# Usage:
# 1. Connect all devices to the same network
# 2. Run the following commands one after another:
#    chmod +x connect_devices_linux.sh
#    ./connect_devices_linux.sh
# 3. Enjoy!
