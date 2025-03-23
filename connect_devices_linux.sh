#!/bin/bash

buttom_str=$(python3 env.py buttom)
top_str=$(python3 env.py top)
if [ -z "$buttom_str" ] || [ -z "$top_str" ]; then
    echo "Error: 'buttom' or 'top' is not set correctly."
    exit 1
fi
for i in $(seq $buttom_str $top_str); do
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
