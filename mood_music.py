
import aiml
import os
import random

# Load AIML kernel
kernel = aiml.Kernel()
kernel.learn("mood.aiml")

print("Welcome to Mood Music 🎵")
while True:
    user_text = input("Tell me how you feel: ")
    if user_text.lower() in ["quit", "exit"]:
        break

    response = kernel.respond(user_text.upper())
    print("Bot:", response)

    # Example: link to your recommender
    if "HAPPY" in user_text.upper():
        songs = ["Happy - Pharrell", "Best Day of My Life - American Authors"]
        print("🎶 Recommended songs:", random.choice(songs))

from textblob import TextBlob
import random



# Songs mapped to moods with YouTube links
songs = {
    "happy": [
        "Pharrell Williams - Happy 🎵 https://youtu.be/ZbZSe6N_BXs",
        "Katrina & The Waves - Walking On Sunshine 🌞 https://youtu.be/iPUmE-tne5U",
        "Justin Timberlake - Can't Stop The Feeling 💃 https://youtu.be/ru0K8uYEZWw"
    ],
    "sad": [
        "Adele - Someone Like You 💔 https://youtu.be/hLQl3WQQoQ0",
        "Lewis Capaldi - Someone You Loved 😢 https://youtu.be/zABLecsR5UE",
        "Billie Eilish - Everything I Wanted 🌙 https://youtu.be/EgBJmlPo8Xw"
    ],
    "angry": [
        "Linkin Park - Numb 🔥 https://youtu.be/kXYiU_JCYtU",
        "Eminem - Lose Yourself 🎤 https://youtu.be/_Yhyp-_hX2s",
        "Metallica - Enter Sandman ⚡ https://youtu.be/CD-E-LDc384"
    ],
    "neutral": [
        "Coldplay - Viva La Vida 🎶 https://youtu.be/dvgZkm1xWPE",
        "Ed Sheeran - Shape of You 🎸 https://youtu.be/JGwWNGJdvx8",
        "Imagine Dragons - Believer 💥 https://youtu.be/7wtfhZwyrcc"
    ]
}

def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # ranges from -1 (negative) to +1 (positive)
    
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    elif "angry" in text.lower() or "mad" in text.lower():
        return "angry"
    else:
        return "neutral"

print("🎧 Welcome to Mood Music! 🎶")
user_text = input("Tell me how you feel right now: ")

mood = detect_mood(user_text)
print(f"\nI think you're feeling: {mood.upper()}")

print("\nHere are some songs for you:")
for song in random.sample(songs[mood], 2):  # show 2 random songs
    print("👉", song)

