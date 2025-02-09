#!/bin/bash

for i in $(seq 40 70); do
    ip="10.0.0.$i"
    echo "Connecting to $ip..."
    adb connect $ip
done
##### to run:
#chmod +x connect_devices_linux.sh
# ./connect_devices_linux.sh