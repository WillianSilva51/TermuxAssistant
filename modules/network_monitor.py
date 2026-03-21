import json
import termux
from pathlib import Path

path = Path("config.json")


def run_wifi_monitor():
    """
    Monitor the current WiFi connection and notify based on network security status.

    This function retrieves information about the currently connected WiFi network,
    compares it against a list of secure networks stored in a JSON file, and sends
    appropriate notifications to the user.

    If the connected network is found in the secure networks list, a notification
    confirming the secure connection is displayed. Otherwise, a notification is sent
    alerting the user that they are not connected to a secure network, followed by
    a device vibration.

    Returns:
        None

    Raises:
        FileNotFoundError: If the JSON file containing secure networks cannot be found.
        json.JSONDecodeError: If the JSON file is malformed.
        KeyError: If the expected keys ("secure_networks" or "ssid") are missing from
                 the JSON file or WiFi info dictionary.

    Note:
        - Requires the termux module to be available.
        - The comparison uses the 'is' operator; consider using '==' for value comparison.
        - The secure networks list should be stored in a JSON file with a "secure_networks"
          key containing a list of network SSIDs.
    """
    wifi = termux.Wifi.info()[1]

    with path.open() as file:
        file_json = json.load(file)
        secure_networks = file_json["secure_networks"]

        ssid = wifi["ssid"]
        for network in secure_networks:
            if ssid is network:
                termux.Notification.notify(
                    title="Secure Network Connected",
                    content=f"You are connected to a secure network: {ssid}",
                )
                return

    termux.Notification.notify(
        title="No Secure Network",
        content="You are not connected to any secure networks.",
    )
    termux.API.vibrate()


if __name__ == "__main__":
    run_wifi_monitor()
