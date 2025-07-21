mood_responses = {
    "happy": ("😊", "That's great to hear! Keep smiling!"),
    "sad": ("😢", "I'm here for you. Things will get better."),
    "angry": ("😠", "Take a deep breath. Let's cool down together."),
    "excited": ("😄", "Yay! I can feel your excitement!"),
    "tired": ("😴", "You deserve some rest. Take care!"),
    "bored": ("😐", "Let's find something fun to do!"),
    "anxious": ("😟", "It's okay to feel anxious. Take it one step at a time."),
    "confused": ("😕", "Don't worry, everything will make sense soon.")
}


user_mood = input("How are you feeling today? ").lower()


if user_mood in mood_responses:
    emoji, message = mood_responses[user_mood]
    print(f"{emoji} {message}")
else:
    
    print("🤔 Hmm... I didn't recognize that mood, but I hope you're doing okay!")