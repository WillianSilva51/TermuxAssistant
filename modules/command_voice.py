import termux
import json
import time


def run_voice_command():
    """
    Execute a voice command and perform corresponding actions.

    This function captures voice input from the user and processes it to
    recognize specific commands. Recognized commands are categorized into
    two types: task-related commands (tarefa, job) and reminder-related
    commands (lembrete, reminder).

    For task commands:
        - Reads the task file path from config.json
        - Appends the spoken command to the task file
        - Provides audio feedback via TTS
        - Handles file writing errors gracefully

    For reminder commands:
        - Schedules a notification reminder
        - Sets the reminder for 60 seconds from the current time
        - Provides audio feedback via TTS

    Returns:
        None

    Raises:
        OSError: If there is an error writing to the task file (caught
                 and handled internally with user notification).
    """
    commands = ["tarefa", "job", "lembrete", "reminder"]

    command = termux.UI.speech(hint="Please speak your command", title="Voice Command")[
        1
    ]["text"]

    if command:
        print(f"You said: {command}")
    else:
        print("No command recognized.")
        return

    for cmd in command.lower().split():
        if cmd in commands[:2]:
            with open("config.json", "r") as f:
                config = json.load(f)
            print(f"Command recognized: {cmd}")
            task_file_path = config["task_file"]
            try:
                with open(task_file_path, "a") as f:
                    f.write(f"{command}\n")
                termux.TTS.tts_speak("Task added.")
            except OSError as e:
                print(f"Error writing to task file: {e}")
                termux.TTS.tts_speak("Error adding task.")
            return
        elif cmd in commands[2:4]:
            print(f"Command recognized: {cmd}")
            termux.Scheduler.schedule(
                termux.Notification.notify(title="Reminder", content=command),
                kwargs={"when": time.time() + 60},
            )
            termux.TTS.tts_speak("Reminder set.")
            return

    print("No valid command found.")


if __name__ == "__main__":
    run_voice_command()
