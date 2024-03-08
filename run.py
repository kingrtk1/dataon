import android

droid = android.Android()

def toggle_wifi():
    wifi_status = droid.checkWifiState().result
    if wifi_status:
        droid.toggleWifiState(False)
        print("WiFi turned off")
    else:
        droid.toggleWifiState(True)
        print("WiFi turned on")

def toggle_mobile_data():
    mobile_data_status = droid.toggleMobileDataState().result
    if mobile_data_status:
        print("Mobile data turned on")
    else:
        print("Mobile data turned off")

def main():
    while True:
        print("1. Toggle WiFi")
        print("2. Toggle Mobile Data")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            toggle_wifi()
        elif choice == 2:
            toggle_mobile_data()
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
