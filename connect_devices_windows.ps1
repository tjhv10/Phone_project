for ($i=64; $i -le 69; $i++) {
    $ip = "10.0.0." + ("{0:D2}" -f $i)
    Write-Host "Connecting to $ip..."
    & adb connect $ip
}
############ to run the script change numbers in the for loop to match your devices ip address ends
# powershell -ExecutionPolicy Bypass -File .\connect_devices.ps1