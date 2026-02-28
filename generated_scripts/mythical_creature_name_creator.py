import random
import tkinter as tk
from tkinter import ttk

class MythicalCreatureNameCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mythical Creature Name Creator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Define word components
        self.prefixes = [
            "Shadow", "Iron", "Crystal", "Thunder", "Ghost", "Flame", 
            "Moon", "Star", "Wind", "Stone", "Dragon", "Dark", "Light",
            "Swift", "Ancient", "Lost", "Forgotten", "Crimson", "Azure",
            "Ruby", "Emerald", "Sapphire", "Obsidian", "Silver", "Gold"
        ]
        
        self.suffixes = [
            "Wing", "Claw", "Scale", "Horn", "Eye", "Heart", "Blood", 
            "Breath", "Fire", "Fang", "Tail", "Spine", "Skin", "Bone",
            "Maw", "Gaze", "Roar", "Song", "Dance", "Flight", "Dream",
            "Night", "Dawn", "Storm", "Tide", "Wave", "Scream"
        ]
        
        self.adjectives = [
            "Terrible", "Incredible", "Magnificent", "Mystic", "Ancient", 
            "Enormous", "Tiny", "Giant", "Small", "Huge", "Little", "Great",
            "Small", "Big", "Gigantic", "Massive", "Humongous", "Petite",
            "Delicate", "Rugged", "Sharp", "Dull", "Shimmering", "Glowing",
            "Pulsing", "Flickering", "Twinkling", "Twisting"
        ]
        
        self.nouns = [
            "Beast", "Creature", "Monster", "Drake", "Dragon", "Wyrm", 
            "Demon", "Angel", "Spirit", "Ghost", "Wraith", "Phantom",
            "Giant", "Titan", "Behemoth", "Leviathan", "Kraken", "Hydra",
            "Unicorn", "Pegasus", "Minotaur", "Centaur", "Mermaid", "Siren"
        ]
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Mythical Creature Name Creator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Instructions
        instructions = ttk.Label(main_frame, text="Click 'Generate Name' to create a ridiculous fantasy creature name!",
                               font=("Arial", 10), foreground="gray")
        instructions.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        # Output frame
        output_frame = ttk.LabelFrame(main_frame, text="Generated Name", padding="10")
        output_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Name display
        self.name_var = tk.StringVar(value="Click Generate to Start!")
        self.name_label = ttk.Label(output_frame, textvariable=self.name_var, 
                                   font=("Arial", 14, "bold"), wraplength=400, justify="center")
        self.name_label.pack()
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        # Generate button
        self.generate_btn = ttk.Button(buttons_frame, text="Generate Name", 
                                     command=self.generate_name, style="Accent.TButton")
        self.generate_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_btn = ttk.Button(buttons_frame, text="Clear", command=self.clear_name)
        self.clear_btn.pack(side=tk.LEFT)
        
        # Stats frame
        stats_frame = ttk.LabelFrame(main_frame, text="Name Components", padding="10")
        stats_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Stats labels
        self.prefix_var = tk.StringVar()
        self.suffix_var = tk.StringVar()
        self.adj_var = tk.StringVar()
        self.noun_var = tk.StringVar()
        
        ttk.Label(stats_frame, text="Prefix:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Label(stats_frame, textvariable=self.prefix_var, font=("Arial", 10, "bold")).grid(row=0, column=1, sticky=tk.W)
        
        ttk.Label(stats_frame, text="Suffix:").grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Label(stats_frame, textvariable=self.suffix_var, font=("Arial", 10, "bold")).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(stats_frame, text="Adjective:").grid(row=2, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Label(stats_frame, textvariable=self.adj_var, font=("Arial", 10, "bold")).grid(row=2, column=1, sticky=tk.W)
        
        ttk.Label(stats_frame, text="Noun:").grid(row=3, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Label(stats_frame, textvariable=self.noun_var, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky=tk.W)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Configure style
        style = ttk.Style()
        style.configure("Accent.TButton", foreground="white", background="#4CAF50")
        
    def generate_name(self):
        # Generate random components
        prefix = random.choice(self.prefixes)
        suffix = random.choice(self.suffixes)
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        
        # Combine components into a name (various patterns)
        patterns = [
            f"{prefix}{suffix}",
            f"{adjective} {noun}",
            f"{prefix} {adjective} {suffix}",
            f"{adjective} {prefix} {suffix}",
            f"{prefix} {noun} of the {adjective} {suffix}",
            f"The {adjective} {prefix} {suffix}",
            f"{prefix}{adjective}{suffix}",
            f"{noun} {suffix} of {prefix}",
            f"The {prefix} {adjective} {noun}"
        ]
        
        name = random.choice(patterns)
        
        # Update display
        self.name_var.set(name)
        
        # Update stats
        self.prefix_var.set(prefix)
        self.suffix_var.set(suffix)
        self.adj_var.set(adjective)
        self.noun_var.set(noun)
        
    def clear_name(self):
        self.name_var.set("Click Generate to Start!")
        self.prefix_var.set("")
        self.suffix_var.set("")
        self.adj_var.set("")
        self.noun_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = MythicalCreatureNameCreator(root)
    root.mainloop()