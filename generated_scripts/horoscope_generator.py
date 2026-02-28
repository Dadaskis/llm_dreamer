import random
import string

def generate_horoscope():
    # Zodiac signs and their traits
    signs = {
        "Aries": "You're energetic and competitive today. Your passion will drive you forward.",
        "Taurus": "Stability and comfort are important. Take time to appreciate what you have.",
        "Gemini": "Communication is key. Your words today will influence others positively.",
        "Cancer": "Emotions are running high. Trust your instincts and inner wisdom.",
        "Leo": "Confidence is your superpower. Shine brightly and inspire others.",
        "Virgo": "Attention to detail will pay off. Organize your thoughts and approach systematically.",
        "Libra": "Balance is essential. Harmony in relationships will bring joy today.",
        "Scorpio": "Transformation is happening. Trust the process and embrace change.",
        "Sagittarius": "Adventure calls. Take risks and explore new horizons with curiosity.",
        "Capricorn": "Ambition and discipline will lead to success. Stay focused on your goals.",
        "Aquarius": "Innovation and originality are highlighted. Your unique ideas will flourish.",
        "Pisces": "Intuition guided by compassion. Your empathy connects you to others."
    }
    
    # Random predictions for variety
    predictions = [
        "A surprising opportunity will present itself.",
        "Your creativity will be recognized today.",
        "A friendship will bring unexpected joy.",
        "Take a moment to reflect on your progress.",
        "Kindness will return to you tenfold.",
        "Your hard work will finally pay off.",
        "A new perspective will change everything.",
        "Trust the journey, even when it's uncertain.",
        "Your positive energy will attract good fortune.",
        "Sometimes less is more. Simplify your approach.",
        "Your intuition is stronger than you know.",
        "A challenge will lead to growth.",
        "Take time for self-care and rejuvenation.",
        "Your natural talents are awakening.",
        "Today is perfect for initiating new projects."
    ]
    
    # Random phrases for creative horoscopes
    phrases = [
        "The stars whisper that",
        "Your cosmic energy suggests",
        "The universe aligns to say",
        "A celestial sign indicates",
        "Your zodiac connection tells",
        "The cosmos reveals",
        "Your astrological essence shows",
        "The heavens suggest",
        "Universal forces say",
        "The stars point toward"
    ]
    
    # Main logic
    print("🔮 ** Horoscope Generator ** 🔮")
    print("Type anything below (or press Enter to randomize):")
    
    user_input = input("> ").strip()
    
    if not user_input:
        # If nothing typed, generate a random horoscope
        sign = random.choice(list(signs.keys()))
        phrase = random.choice(phrases)
        prediction = random.choice(predictions)
        
        print(f"\n✨ {phrase} {prediction}")
        print(f"🌟 {sign}: {signs[sign]}")
        print("\nMay your day be filled with cosmic blessings! 🌌")
        
    else:
        # Use typing as input to generate personalized horoscope
        
        # Use character counts to determine mood/traits
        char_count = len(user_input)
        vowel_count = sum(1 for c in user_input.lower() if c in 'aeiou')
        consonant_count = sum(1 for c in user_input.lower() if c in string.ascii_lowercase and c not in 'aeiou')
        
        # Select a sign based on input patterns
        if char_count < 5:
            sign = "Aries" if vowel_count > consonant_count else "Taurus"
        elif char_count < 10:
            sign = "Gemini" if vowel_count > consonant_count else "Cancer"
        elif char_count < 15:
            sign = "Leo" if vowel_count > consonant_count else "Virgo"
        else:
            sign = "Scorpio" if vowel_count > consonant_count else "Sagittarius"
        
        # Select prediction based on input
        if random.random() < 0.3:  # 30% chance for a different full prediction
            phrase = random.choice(phrases)
            prediction = random.choice(predictions)
            print(f"\n✨ {phrase} {prediction}")
            print(f"🌟 {sign}: {signs[sign]}")
        else:
            # Combine regular information with dynamic elements
            if len(user_input) < 3:
                prediction = "Your brief message carries great meaning. Focus on quality over quantity."
            elif len(user_input) < 8:
                prediction = "Your words are becoming more meaningful with each character."
            else:
                prediction = "Your thoughtful typing shows you're ready to receive cosmic guidance."
            
            # Dynamic sign selection based on some logic
            alphabet_count = sum(1 for c in user_input.lower() if c.isalpha())
            if alphabet_count % 2 == 0:
                sign = random.choice(list(signs.keys()))
            else:
                sign = random.choice(["Pisces", "Aquarius", "Libra"]) if vowel_count > consonant_count else random.choice(["Capricorn", "Scorpio", "Sagittarius"])
            
            print(f"\n✨ Your keystrokes revealed: {prediction}")
            print(f"🌟 {sign}: {signs[sign]}")
        
        print("\nMay your typing spell success! ✨")

if __name__ == "__main__":
    generate_horoscope()