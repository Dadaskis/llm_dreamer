import tkinter as tk
from tkinter import scrolledtext
import random

class HorrorStoryCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Horror Story Creator")
        self.root.geometry("600x500")
        
        # Story components
        self.adjectives = ["creepy", "sinister", "horrifying", "macabre", "ghastly", "terrible", "dreadful", "spine-chilling", "nightmarish", "unspeakable"]
        self.animals = ["werewolf", "zombie", "vampire", "ghost", "monster", "demon", "werewolf", "shadow creature", "cursed being", "abomination"]
        self.foods = ["pizza", "ice cream", "burgers", "sushi", "tacos", "pasta", "cookies", "cake", "chocolate", "noodles"]
        self.locations = ["abandoned asylum", "haunted forest", "derelict mansion", "old cemetery", "dark alley", "isolated cabin", "forgotten cave", "abandoned school", "ruined church", "deserted hotel"]
        self.actions = ["chases", "attacks", "haunts", "terrifies", "possesses", "devours", "lurks", "screams", "whispers", "dances"]
        self.personalities = ["who loves", "who hates", "who dreams of", "who fears", "who remembers", "who forgets", "who desires", "who refuses", "who accepts", "who rejects"]
        self.verbs = ["screams", "whispers", "moans", "laughs", "sobs", "cries", "shrieks", "growls", "roars", "whispers"]
        self.situations = ["at midnight", "in the rain", "during a storm", "under the full moon", "in the dark", "in the shadows", "on Halloween", "at dawn", "at sunrise", "during thunder"]
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Random Horror Story Creator", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Story display area
        self.story_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
        self.story_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Generate button
        generate_button = tk.Button(self.root, text="Generate Horror Story", command=self.generate_story, font=("Arial", 12, "bold"), bg="#ff6b6b", fg="white")
        generate_button.pack(pady=10)
        
        # Add some initial text
        self.story_text.insert(tk.END, "Click the button to generate a random horror story!\n\n")
        
    def generate_story(self):
        # Clear previous story
        self.story_text.delete(1.0, tk.END)
        
        # Generate story components
        story_parts = []
        
        # Part 1: Setup
        adj1 = random.choice(self.adjectives)
        animal = random.choice(self.animals)
        food = random.choice(self.foods)
        loc1 = random.choice(self.locations)
        
        part1 = f"A {adj1} {animal} who likes {food} was spotted in the {loc1}."
        story_parts.append(part1)
        
        # Part 2: Action
        action = random.choice(self.actions)
        adj2 = random.choice(self.adjectives)
        loc2 = random.choice(self.locations)
        
        part2 = f"Someone saw it {action} people in the {loc2} in the {adj2} night."
        story_parts.append(part2)
        
        # Part 3: Personality
        personality = random.choice(self.personalities)
        verb = random.choice(self.verbs)
        situation = random.choice(self.situations)
        
        part3 = f"The {animal} {personality} {random.choice(self.foods)} and {verb} {situation}."
        story_parts.append(part3)
        
        # Part 4: Twist
        animal2 = random.choice(self.animals)
        adj3 = random.choice(self.adjectives)
        loc3 = random.choice(self.locations)
        
        part4 = f"However, it turns out that the {animal2} was actually a {adj3} {animal} that was just {random.choice(['protecting', 'helping', 'searching', 'watching'])} the {loc3}."
        story_parts.append(part4)
        
        # Part 5: Climax
        action2 = random.choice(self.actions)
        adj4 = random.choice(self.adjectives)
        verb2 = random.choice(self.verbs)
        
        part5 = f"Then suddenly, it {action2} everyone with a {adj4} {random.choice(['scream', 'outburst', 'howl', 'wail'])} that made the {verb2} all around."
        story_parts.append(part5)
        
        # Part 6: Ending
        ending = random.choice([
            "The horror became too much to bear for those who witnessed it.",
            "The next morning, only the echoes of that terrifying night remained.",
            "The {animal} disappeared into shadows and has not been seen since.",
            "The {animal} was deemed too dangerous and was hunted by the authorities.",
            "That night, the {animal} had finally found its true purpose."
        ])
        
        # Insert all parts into the story
        story_text = "\n".join(story_parts)
        story_text = story_text.replace("{animal}", random.choice(self.animals))
        
        self.story_text.insert(tk.END, story_text)
        self.story_text.insert(tk.END, "\n\nTHE END\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HorrorStoryCreator(root)
    root.mainloop()