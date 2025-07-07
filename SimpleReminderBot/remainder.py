import speech_recognition as sr
import pyttsx3
import time
import re
from plyer import notification

# === Initialize engines ===
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening for reminder...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            speak("Sorry, I didn’t catch that.")
            return ""

def parse_command(command):
    # Example: "remind me to take medicine in 2 minutes"
    task_match = re.search(r"remind me to (.+?) in", command)
    time_match = re.search(r"in (\d+) (minute|minutes|second|seconds)", command)

    if task_match and time_match:
        task = task_match.group(1).strip()
        amount = int(time_match.group(1))
        unit = time_match.group(2)

        seconds = amount * 60 if "minute" in unit else amount
        return task, seconds
    else:
        return None, None

def remind(task):
    notification.notify(
        title="🔔 Reminder",
        message=f"Time for: {task}",
        timeout=10
    )
    speak(f"Reminder: {task}")
    print("✅ Reminder delivered!")

# === Main Bot Logic ===
def main():
    speak("What would you like me to remind you about?")
    command = listen()
    task, wait_time = parse_command(command)

    if task and wait_time:
        speak(f"Setting reminder for {task} in {wait_time // 60 if wait_time >= 60 else wait_time} seconds.")
        print(f"⏳ Waiting for {wait_time} seconds...")
        time.sleep(wait_time)
        remind(task)
    else:
        speak("Sorry, I couldn't understand. Please try again.")

if __name__ == "__main__":
    main()