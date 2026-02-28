import random
import tkinter as tk
from tkinter import ttk

class FakeNewsHeadlineMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake News Headline Maker")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')
        
        # Sample word lists
        self.adjectives = [
            "Shocking", "Bizarre", "Incredible", "Unbelievable", "Mind-Bending",
            "Alarming", "Terrifying", "Amazing", "Disgusting", "Horrifying",
            "Revolutionary", "Dramatic", "Scandalous", "Controversial", "Secret",
            "Surprising", "Unexpected", "Catastrophic", "Mysterious", "Eerie"
        ]
        
        self.nouns = [
            "Government", "Scientists", "Children", "Animals", "Technology",
            "Food", "Weather", "Sports", "Music", "Movies",
            "Celebrities", "Politicians", "Doctors", "Teachers", "Students",
            "Animals", "Plants", "Cars", "Computers", "Companies"
        ]
        
        self.verbs = [
            "Invents", "Discovers", "Develops", "Creates", "Builds",
            "Finds", "Uncover", "Reveals", "Announces", "Reports",
            "Confirms", "Proves", "Proves", "Believes", "Claims",
            "Says", "Claims", "Swears", "Insists", "States"
        ]
        
        self.mundane_topics = [
            "school lunches", "cat food", "traffic jams", "garden hoses", 
            "socks", "umbrellas", "coffee shops", "library books", 
            "park benches", "shopping malls", "supermarkets", "bus stops",
            "restaurant menus", "phone apps", "fitness equipment", "toothpaste",
            "haircuts", "house plants", "car insurance", "bathroom scales"
        ]
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Fake News Headline Maker", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Display area
        self.display_frame = tk.Frame(main_frame, bg='white', relief='sunken', borderwidth=2)
        self.display_frame.pack(expand=True, fill='both', pady=10)
        
        self.headline_label = tk.Label(
            self.display_frame,
            text="Press 'Generate Headline' to create a fake headline",
            font=("Arial", 14),
            wraplength=500,
            bg='white',
            fg='#222222'
        )
        self.headline_label.pack(expand=True, pady=30)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='#f0f0f0')
        buttons_frame.pack(fill='x', pady=10)
        
        # Generate button
        self.generate_button = tk.Button(
            buttons_frame,
            text="Generate Headline",
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=10,
            command=self.generate_headline
        )
        self.generate_button.pack(side='left', padx=10)
        
        # Clear button
        clear_button = tk.Button(
            buttons_frame,
            text="Clear",
            font=("Arial", 12),
            bg='#f44336',
            fg='white',
            padx=20,
            pady=10,
            command=self.clear_headline
        )
        clear_button.pack(side='left', padx=10)
        
        # Info text
        info_label = tk.Label(
            main_frame,
            text="Generate ridiculous headlines about mundane topics!",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666666'
        )
        info_label.pack(pady=10)
        
    def generate_headline(self):
        # Randomly choose words
        adj1 = random.choice(self.adjectives)
        adj2 = random.choice(self.adjectives)
        noun1 = random.choice(self.nouns)
        verb = random.choice(self.verbs)
        noun2 = random.choice(self.nouns)
        topic = random.choice(self.mundane_topics)
        
        # Create headline
        headline = f"{adj1} {adj2} {noun1} {verb} {noun2} About {topic}"
        
        # Display headline with formatting
        self.headline_label.config(
            text=headline,
            font=("Arial", 16, "bold")
        )
        
    def clear_headline(self):
        self.headline_label.config(
            text="Press 'Generate Headline' to create a fake headline",
            font=("Arial", 14)
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeNewsHeadlineMaker(root)
    root.mainloop()