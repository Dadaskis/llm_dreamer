import random
import datetime

def generate_fortune():
    # Randomly generated data for fortune telling
    fortunes = [
        "You will meet someone who believes in aliens, but only after they've already been to Mars.",
        "Your lucky number is 42, which is also the answer to life, the universe, and everything, except that's not really true.",
        "A stranger will offer you a sandwich, but you'll reject it because you're not hungry, yet somehow you're very hungry.",
        "You will find a coin that is both heads and tails simultaneously, but it will be on the ground and you'll be in a hurry.",
        "Your crush will text you first, but it will be about an unrelated topic and not about you at all.",
        "You'll win a contest for 'most likely to trip over your own shoelaces,' and everyone will think it's a joke.",
        "You'll have an excellent day, which means you'll get into exactly the wrong arguments with exactly the right people.",
        "A cat will knock over your coffee cup, then stare at you with the most smug expression imaginable.",
        "You'll get a call from a number you don't recognize but will somehow relate to your deepest fears.",
        "You'll be offered a promotion, but it involves being the official spokesperson for a very strange local business.",
        "You'll suddenly remember how to play the piano, but only to play that one annoying tune that everyone loves.",
        "A mysterious package will arrive at your door with no return address and a message that says 'the end is near.'",
        "Your dog will develop a habit of staring at you like you're a very interesting piece of furniture.",
        "You'll make a life-changing decision in the middle of a very embarrassing situation.",
        "You'll find a wallet full of cash, but it will be too much to be true, and you'll lose it before you can count it.",
        "You'll meet your future spouse, but they'll be wearing something ridiculous and will be very upset about it.",
        "You'll have a brilliant idea while in the middle of doing something completely unrelated, like brushing your teeth.",
        "You'll receive a gift that's exactly what you've always wanted, but your pet will destroy it before you can open it.",
        "You'll be complimented on your cooking, but it will be because someone else's food smells like yours.",
        "You'll get a job offer that's too good to be true, but it involves working for the government's comedy department."
    ]
    
    # Random elements for variety
    random_elements = [
        "In a month of your choosing, you will find a treasure map in the back of a local supermarket.",
        "Your reflection in the mirror will give you advice you've never asked for.",
        "You will have an amazing day, but you'll also have an amazing day.",
        "You're going to have a very good day, except for the part where you forget to have the good day.",
        "You will be recognized as the world's greatest expert on the history of cheese.",
        "The day will begin with a small problem, but you'll end up solving a global crisis.",
        "You'll find a coin from the 19th century, but it will be a fake you'll never be able to tell.",
        "Your lucky day will come on a Tuesday, but you'll forget it's a Tuesday.",
        "You'll suddenly know the answer to everything, but it will make no sense.",
        "Your day will be filled with unexpected joy and a very confusing pizza situation."
    ]
    
    # Generate a random fortune
    fortune = random.choice(fortunes)
    
    # Add a random element for extra hilarity
    bonus = random.choice(random_elements)
    
    # Add a random prediction based on today's date
    today = datetime.date.today()
    day_of_week = today.strftime("%A")
    month = today.strftime("%B")
    year = today.year
    
    date_info = f"By the way, today is {day_of_week}, {month} {today.day}, {year}, so you're definitely going to be okay."
    
    # Combine all elements
    full_fortune = f"{fortune}\n{bonus}\n{date_info}"
    
    return full_fortune

def main():
    print("🔮 Welcome to the Hilariously Wrong Fortune Teller! 🔮")
    print("Enter 'quit' to exit")
    print()
    
    while True:
        user_input = input("Ask your fortune (or press Enter for a random one): ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thanks for consulting the fortune teller! (Or was it a fortune mocker?)")
            break
            
        # Generate a new fortune each time
        print("\n✨ Your hilarious fortune: ✨")
        print(generate_fortune())
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()