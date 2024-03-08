import subprocess
import time

def check_wifi_status():
    result = subprocess.run(["termux-wifi-connectioninfo"], capture_output=True, text=True)
    connection_info = result.stdout.strip().split("\n")
    if len(connection_info) > 1 and "state: CONNECTED" in connection_info[1]:
        return True
    return False

def toggle_mobile_data(enable):
    action = "enable" if enable else "disable"
    subprocess.run(["termux-sensor", "-s", "accelerometer", action])  # Turn on/off mobile data sensors

def main():
    wifi_connected = False
    while True:
        print("Running...")
        new_wifi_status = check_wifi_status()
        if not wifi_connected and new_wifi_status:
            print("WiFi connected. Turning off sensors.")
            toggle_mobile_data(False)  # Turn off sensors when WiFi connects
            wifi_connected = True
        elif wifi_connected and not new_wifi_status:
            print("WiFi connection lost. Turning on sensors.")
            toggle_mobile_data(True)  # Turn on sensors when WiFi disconnects
            wifi_connected = False
        time.sleep(1)  # Check every 10 seconds

if __name__ == "__main__":
    main()
