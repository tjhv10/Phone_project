for ($i=33; $i -le 40; $i++) {
    $ip = "10.0.0." + ("{0:D2}" -f $i)
    Write-Host "Connecting to $ip..."
    & adb connect $ip
}
# powershell -ExecutionPolicy Bypass -File .\connect_devices.ps1    ############to run the script change numbers in the for loop to match your devices