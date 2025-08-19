import termux, json, time

def run_voice_command():
    commands = ['tarefa', 'job', 'lembrete', 'reminder']

    command = termux.UI.speech(
        hint="Please speak your command",
        title="Voice Command")[1]['text']
    
    if command:
        print(f"You said: {command}")
    else:
        print("No command recognized.")
        return

    for cmd in command.lower().split():
        if cmd in commands[:2]:
            with open('config.json', 'r') as f:
                config = json.load(f)
            print(f"Command recognized: {cmd}")
            task_file_path = config['task_file']
            try:
                with open(task_file_path, 'a') as f:
                    f.write(f"{command}\n")
                termux.TTS.tts_speak("Task added.")
            except OSError as e:
                print(f"Error writing to task file: {e}")
                termux.TTS.tts_speak("Error adding task.")
            return
        elif cmd in commands[2:4]:
            print(f"Command recognized: {cmd}")
            termux.Scheduler.schedule(termux.Notification.notify(
                title="Reminder",
                content=command), kwargs={"when": time.time() + 60})
            termux.TTS.tts_speak("Reminder set.")
            return

    print("No valid command found.")

if __name__ == "__main__":
    run_voice_command()