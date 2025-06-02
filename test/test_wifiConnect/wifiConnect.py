import subprocess

ssid = "LAB821(AI&ASIC)"
password = "deucomputer821"

# result = subprocess.run(
#     ["sudo", "nmcli", "device", "wifi", "connect", ssid, "password", password],
#     capture_output=True,
# )

result = subprocess.run(["sudo", "nmcli", "device", "disconnect", "wlan0"])

print(result.returncode)
