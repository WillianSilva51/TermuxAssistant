import argparse
from modules import dashboard, command_voice, network_monitor

def main():
    parser = argparse.ArgumentParser(description='Assistant CLI Tool')
    parser.add_argument('--dashboard', action='store_true', help='Run the dashboard')
    parser.add_argument('--voice', action='store_true', help='Run the voice command interface')
    parser.add_argument('--wifi', action='store_true', help='Run the WiFi network monitor')
    
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        parser.print_help()
        return
    
    if args.dashboard:
        dashboard.run_dashboard()
    if args.voice:
        command_voice.run_voice_command()
    if args.wifi:
        network_monitor.run_wifi_monitor()

if __name__ == "__main__":
    main()