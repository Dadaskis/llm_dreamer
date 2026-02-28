import random
import tkinter as tk
from tkinter import ttk

class RandomMoviePlotGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Movie Plot Generator")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Define word lists
        self.genres = [
            "Sci-fi", "Horror", "Romance", "Comedy", "Action", 
            "Adventure", "Mystery", "Fantasy", "Thriller", "Western"
        ]
        
        self.settings = [
            "in the year 2050", "in a dystopian future", "in a parallel universe", 
            "on a distant planet", "in a post-apocalyptic world", "in a fairy tale kingdom",
            "in a futuristic city", "in a remote village", "in a magical forest", 
            "during a solar eclipse", "in a parallel dimension", "in a futuristic ocean"
        ]
        
        self.actors = [
            "a robot", "a time traveler", "a vampire", "a werewolf", 
            "an alien", "a wizard", "a detective", "a chef", "a billionaire",
            "a zombie", "a mermaid", "a superhero", "a cat burglar", "a space explorer"
        ]
        
        self.character_traits = [
            "who's afraid of the moon", "who's allergic to laughter", 
            "who's a perfectionist", "who's afraid of the dark", 
            "who's a closet romantic", "who's allergic to water", 
            "who's a notorious liar", "who's afraid of heights", 
            "who's a recovering alcoholic", "who's a genius", 
            "who's a pessimist", "who's a conspiracy theorist"
        ]
        
        self.actions = [
            "falls in love with", "must save", "discovers", "chases", 
            "accidentally destroys", "must escape from", "stumbles upon", 
            "must solve", "investigates", "must protect", "travels to", 
            "faces off against", "must master", "finds out about", 
            "is betrayed by", "must become", "uncover the secret of"
        ]
        
        self.objects = [
            "a dying star", "the cure for aging", "a time machine", 
            "a hidden treasure", "the last pizza", "the key to immortality",
            "a lost civilization", "a mysterious letter", "an antique clock",
            "a forbidden spell", "the source of all power", "a portal to another dimension",
            "a broken heart", "a secret organization", "a powerful artifact"
        ]
        
        self.conflicts = [
            "before time runs out", "in a race against evil", 
            "while dealing with family issues", "despite everything", 
            "in a battle for justice", "despite personal fears", 
            "in a world where everything is backwards", "despite social expectations", 
            "in a relationship that's doomed", "despite all logic", 
            "while being hunted by authorities", "in a world that's ending"
        ]
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Random Movie Plot Generator", 
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Generate button
        generate_button = tk.Button(
            self.root,
            text="Generate Random Plot",
            font=("Arial", 16, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            command=self.generate_plot
        )
        generate_button.pack(pady=20)
        
        # Plot display area
        self.plot_text = tk.Text(
            self.root,
            height=15,
            width=60,
            font=("Arial", 12),
            bg="white",
            fg="#2c3e50",
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        self.plot_text.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.plot_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.plot_text.configure(yscrollcommand=scrollbar.set)
        
        # Insert initial text
        self.plot_text.insert(tk.END, "Click 'Generate Random Plot' to create an absurd movie plot!\n\n")
        self.plot_text.insert(tk.END, "Example: 'A sci-fi romance about a robot who's afraid of the moon must save the last pizza from a time traveler in a futuristic city.'")
        
    def generate_plot(self):
        # Generate random elements
        genre1 = random.choice(self.genres)
        genre2 = random.choice(self.genres)
        setting = random.choice(self.settings)
        actor = random.choice(self.actors)
        trait = random.choice(self.character_traits)
        action = random.choice(self.actions)
        object_ = random.choice(self.objects)
        conflict = random.choice(self.conflicts)
        
        # Create the plot
        plot_template = (
            f"A {genre1} {genre2} about {actor} {trait} {action} {object_} {conflict}.\n\n"
            f"Genre: {genre1} + {genre2}\n"
            f"Setting: {setting}\n"
            f"Main Character: {actor} ({trait})\n"
            f"Main Action: {action} {object_}\n"
            f"Conflict: {conflict}"
        )
        
        # Clear and insert new plot
        self.plot_text.delete(1.0, tk.END)
        self.plot_text.insert(tk.END, plot_template)
        
        # Add some extra fun
        fun_facts = [
            "This plot is entirely random and may not make sense!",
            "This could be the next bestseller!",
            "The movie has a 99% chance of being a box office flop!",
            "Watch out for unexpected plot twists!",
            "This title has not been trademarked yet!"
        ]
        self.plot_text.insert(tk.END, f"\n\nFun Fact: {random.choice(fun_facts)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomMoviePlotGenerator(root)
    root.mainloop()