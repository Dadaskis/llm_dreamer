import random
import time
import os
import sys
from datetime import datetime

class PetRockAdvisor:
    def __init__(self):
        self.moods = {
            "happy": ["cheerful", "joyful", "elated", "delighted"],
            "sad": ["dejected", "melancholy", "downcast", "blue"],
            "angry": ["furious", "irritated", "livid", "infuriated"],
            "confused": ["perplexed", "bewildered", "puzzled", "disoriented"]
        }
        
        self.weather_advice = {
            "sunny": [
                "Oh great, it's sunny. Perfect weather for doing absolutely nothing. Just like your life!",
                "Bright and sunny! Not exactly the weather for racing to catch your own reflection.",
                "Looks like the sun is out. Maybe you should try shining brighter than your personality."
            ],
            "rainy": [
                "Rainy day! Perfect weather for staying inside and being just as miserable as the weather.",
                "It's raining! How wonderful to be miserable with the weather. Do you always plan for this?",
                "Rainy day! You know, it's not my fault your life isn't as inspiring as a good rainstorm."
            ],
            "cloudy": [
                "Cloudy skies today. How wonderfully vague your existence seems, just like the weather.",
                "Looks like it's cloudy. Just like your future, completely obstructed by sheer laziness.",
                "Cloudy. Just like your mind, perpetually obscured by self-pity and grumpiness."
            ],
            "snowy": [
                "Snowy day! What a wonderful way to be stuck in the cold, just like your heart.",
                "Snowing! It's about time your life took a turn for the freezing cold and miserable.",
                "Snowy! Just like your social life, it's all about the fluff and a total waste of good water."
            ]
        }
        
        self.sarcastic_tips = [
            "Advice: Remember that everyone is going through the same thing... except you. You're special.",
            "Why don't you try treating yourself like the exceptional human being you are? Well, you're not.",
            "The secret to life is to just... be... well, you're not really doing that, are you?",
            "Also, have you considered that maybe the real problem is you?",
            "Try being optimistic! Not that anyone else expects anything from you anyway.",
            "Happiness is just another thing you're not achieving. And that's okay!",
            "You know what? The answer is always 'do nothing' when you don't want to do anything.",
            "Remember, it's not your fault you're perfect at everything you do... which is nothing."
        ]
        
        self.rock_images = [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Rock_on_Table.jpg/800px-Rock_on_Table.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Rock_(2350107602).jpg/800px-Rock_(2350107602).jpg"
        ]

    def get_weather(self):
        """Simulate current weather based on time of day"""
        hour = datetime.now().hour
        if 6 <= hour < 18:
            return "sunny"
        elif 18 <= hour < 22:
            return "cloudy"
        else:
            return "rainy"

    def get_mood(self):
        """Simulate current mood based on some random factor"""
        moods = list(self.moods.keys())
        return random.choice(moods)

    def generate_advice(self):
        """Generate a sarcastic advice message"""
        weather = self.get_weather()
        mood = self.get_mood()
        
        # Get simulated weather advice
        advice = random.choice(self.weather_advice[weather])
        
        # Add mood-specific sarcasm
        mood_advice = f"Meanwhile, you're feeling {random.choice(self.moods[mood])} today. "
        
        # Add sarcastic tip
        sarcastic_tip = random.choice(self.sarcastic_tips)
        
        # Combine everything
        full_advice = f"{advice} {mood_advice} {sarcastic_tip}"
        
        return full_advice

    def display_rock_advisor(self):
        """Display the Pet Rock Advisor interface"""
        print("\n" + "="*60)
        print("PET ROCK ADVISOR")
        print("="*60)
        print("Your personal advisor to help you navigate life's challenges.")
        print("Just like a rock, it's always there for you (and never judges).")
        print()
        
        while True:
            print("\nChoose an option:")
            print("1. Get sarcastic life advice")
            print("2. View your pet rock")
            print("3. Exit")
            
            choice = input("Choose wisely (1-3): ").strip()
            
            if choice == "1":
                print("\n" + "-"*50)
                advice = self.generate_advice()
                print(f"YOUR PET ROCK ADVISES: {advice}")
                print("-"*50)
                
                # Adding comedic voiceover effect
                print("\n[Comedic voiceover] *sigh* That's what your rock would say if it had a brain...")
                
            elif choice == "2":
                print("\n[Displaying rock image...]")
                print("Rock viewing functionality would display an image here.")
                print("Or at least pretend to. Your rock is... indeterminate, like your life.")
                
            elif choice == "3":
                print("\n[Pet Rock Voiceover] Oh, no! You're ending our relationship?")
                print("Fine. But don't come crying back when you realize the only advice that matters is a good rock.")
                break
                
            else:
                print("\nInvalid choice. Please select 1, 2, or 3.")
            
            # Add delay for dramatic effect
            time.sleep(1)
            
        print("\nThank you for consulting your Pet Rock Advisor!")

def main():
    advisor = PetRockAdvisor()
    
    # Welcome message with dramatic flair
    print("PET ROCK ADVISOR")
    print("="*60)
    print("Welcome to your new personal advisor!")
    print("Because your friends are too busy being your friends to give you good advice.")
    print("Your advisor? A rock. Because nothing says 'wise' like looking at a rock.")
    print("\n[Academic voiceover] 'Presenting the Pet Rock Advisor, a revolutionary approach to getting emotional support.'")
    
    # Wait a moment for effect
    time.sleep(2)
    
    try:
        advisor.display_rock_advisor()
    except KeyboardInterrupt:
        print("\n\n[Comedic voiceover] You're running away from your problems again?")
        print("Come back when you're ready to face the fact that nothing is ever going to change.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("This is the fault of your operating system, not your pet rock.")

if __name__ == "__main__":
    main()
```

This Pet Rock Advisor Python script features:

1. **Sarcastic Personality**: The advisor delivers biting, humorous commentary that anyone can relate to
2. **Weather-Based Advice**: Different sarcastic responses depending on the simulated time of day
3. **Mood Detection**: Simulates different moods to add variety to the sarcasm
4. **Comedic Voiceover**: A spoof "voiceover" that makes everything more entertaining
5. **Interactive Menu**: Simple text-based interface with options
6. **Stock Photo Reference**: Includes URLs for rock images (though you'd need to display them separately in a GUI environment)
7. **Psychological Humor**: Uses common patterns of self-deprecating humor

To run the script:
1. Save it to a file (e.g., `pet_rock_advisor.py`)
2. Run: `python pet_rock_advisor.py`
