import json, termux

def run_wifi_monitor():
    wifi = termux.Wifi.info()[1]

    secure_networks = json.load(open("config.json"))["secure_networks"]

    ssid = wifi['ssid']
    for network in secure_networks:
        if ssid == network:
            termux.Notification.notify(
                title="Secure Network Connected",
                content=f"You are connected to a secure network: {ssid}"
            )
            return
    
    termux.Notification.notify(
        title="No Secure Network",
        content="You are not connected to any secure networks."        
    )
    termux.API.vibrate()

if __name__ == "__main__":
    run_wifi_monitor()