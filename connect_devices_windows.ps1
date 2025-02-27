for ($i=40; $i -le 70; $i++
) {
    $ip = "10.0.0." + ("{0:D1}" -f $i)
    Write-Host "Connecting to $ip..."
    & adb connect $ip
}
############ to run the script change numbers in the for loop to match your devices ip address endsprun
# powershell -ExecutionPolicy Bypass -File .\connect_devices_windows.ps1