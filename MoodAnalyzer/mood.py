import json
from datetime import datetime
import os

mood_keywords={
    "happy":["happy","joy","great","good","awesome","glad","😀","😄","😁","☺️","😊"],
    "sad":["sad","mad","furious","🥲","😔","😭","☹️","🥹","🥺","upset","bad","hurt"],
    "angry":["angry", "mad", "furious", "😠", "😡"],
    "anxious": ["nervous", "anxious", "worried", "😰", "😟"],
    "excited": ["excited", "thrilled", "can't wait", "😆", "🤩"]
}

# Responses based on mood
mood_responses = {
    "happy": "That's wonderful to hear! Keep spreading the positivity! 😊",
    "sad": "I'm sorry you're feeling this way. Remember: This too shall pass. 💙",
    "angry": "Take a deep breath. It's okay to feel angry, just don’t let it consume you. 🔥",
    "anxious": "You’re doing better than you think. One step at a time. 🧘‍♂️",
    "excited": "Yay! Keep that energy going! 🌟",
    "unknown": "Thanks for sharing. Writing things down always helps. 📝"
}

# Function to detect mood
def detect_mood(entry):
    entry_lower = entry.lower()
    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            if keyword in entry_lower:
                return mood
    return "unknown"

# Function to save entry
def save_entry(entry, mood):
    diary_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entry": entry,
        "mood": mood
    }

    data = []
    if os.path.exists("mood_journal.json"):
        try:
            with open("mood_journal.json", "r") as file:
                content = file.read().strip()
                if content:
                    data = json.loads(content)
        except json.JSONDecodeError:
            print("⚠️ Warning: JSON file was empty or corrupted. Starting fresh.")
            data = []

    data.append(diary_entry)

    with open("mood_journal.json", "w") as file:
        json.dump(data, file, indent=4)


# Main program
def main():
    print("📝 Welcome to Your Mood Journal!")
    entry = input("How are you feeling today? Write a few lines:\n> ")

    mood = detect_mood(entry)
    response = mood_responses.get(mood, mood_responses["unknown"])
    
    print(f"\n🤖 MoodBot: {response}")
    save_entry(entry, mood)
    print("✅ Your entry has been saved. See you tomorrow!")

main()