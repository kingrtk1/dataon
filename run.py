import subprocess
import time

def check_wifi_status():
    result = subprocess.run(["termux-wifi-connectioninfo"], capture_output=True, text=True)
    connection_info = result.stdout.strip().split("\n")
    if len(connection_info) > 1 and "state: CONNECTED" in connection_info[1]:
        return True
    return False

def activate_mobile_data():
    subprocess.run(["termux-tts-speak", "Activating mobile data"])

    # Run Termux API command to enable mobile data
    subprocess.run(["termux-sensor", "-s", "accelerometer"])

def deactivate_mobile_data():
    subprocess.run(["termux-tts-speak", "Deactivating mobile data"])

    # Run Termux API command to disable mobile data
    subprocess.run(["termux-sensor", "-s", "accelerometer"])

def main():
    mobile_data_activated = False
    while True:
        print("Running...")
        wifi_connected = check_wifi_status()
        if not wifi_connected and not mobile_data_activated:
            print("Waiting for connection to be lost...")
            activate_mobile_data()
            mobile_data_activated = True
        elif wifi_connected and mobile_data_activated:
            print("WiFi connection restored. Deactivating mobile data...")
            deactivate_mobile_data()
            mobile_data_activated = False
        time.sleep(1)  # Check every 10 seconds

if __name__ == "__main__":
    main()
