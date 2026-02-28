import random
import tkinter as tk
from tkinter import ttk

class RandomClothingCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Clothing Item Creator")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")
        
        # Clothing categories
        self.clothing_items = {
            "Footwear": ["sneakers", "boots", "sandals", "flip-flops", "high heels", "platform shoes", "ankle boots", "loafers", "combat boots", "wedges"],
            "Upper Body": ["t-shirt", "hoodie", "jacket", "dress", "blouse", "sweater", "suit coat", "tank top", "cardigan", "corsage"],
            "Lower Body": ["jeans", "skirt", "pants", "shorts", "leggings", "dress pants", "cargo pants", "overalls", "culottes", "hot pants"],
            "Headwear": ["baseball cap", "beanie", "bowler hat", "top hat", "beret", "cowboy hat", "fedora", "headband", "scarf", "crown"],
            "Accessories": ["watch", "ring", "necklace", "bracelet", "earrings", "belt", "tie", "gloves", "socks", "socks with tights"]
        }
        
        # Absurd objects to pair with clothing
        self.absurd_objects = ["banana", "pineapple", "watermelon", "chicken", "cactus", "sushi", "pizza", "penguin", "unicorn", "spaceship", "teddy bear", "umbrella", "fire hydrant", "carrot", "rubber duck"]
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Random Clothing Item Creator", font=("Arial", 18, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        # Description
        desc_label = tk.Label(self.root, text="Generate absurd outfit combinations!", font=("Arial", 12), bg="#f0f0f0")
        desc_label.pack(pady=5)
        
        # Outfit display frame
        outfit_frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        outfit_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Outfit label
        self.outfit_label = tk.Label(outfit_frame, text="Press 'Create Outfit' to generate a combination!", 
                                   font=("Arial", 14), wraplength=400, bg="#ffffff", fg="#333333")
        self.outfit_label.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        # Create outfit button
        create_btn = tk.Button(button_frame, text="Create Outfit", command=self.generate_outfit, 
                             font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=10)
        create_btn.pack(side=tk.LEFT, padx=10)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_outfit, 
                            font=("Arial", 12), bg="#f44336", fg="white", padx=20, pady=10)
        clear_btn.pack(side=tk.LEFT, padx=10)
        
        # Footer
        footer_label = tk.Label(self.root, text="WARNING: This is for entertainment purposes only!", 
                              font=("Arial", 10), bg="#f0f0f0", fg="#666666")
        footer_label.pack(pady=10)
    
    def generate_outfit(self):
        # Create an outfit with one item from each category plus an absurd object
        outfit_parts = []
        
        # Add items from each category
        for category, items in self.clothing_items.items():
            item = random.choice(items)
            outfit_parts.append(item)
        
        # Add an absurd object
        absurd_object = random.choice(self.absurd_objects)
        outfit_parts.append(f"and a {absurd_object}")
        
        # Create the outfit string
        outfit = ", ".join(outfit_parts[:-1]) + f" with a {absurd_object}"
        
        # Display the outfit (with text wrapping)
        self.outfit_label.config(text= outfit, wraplength=400)
        
    def clear_outfit(self):
        self.outfit_label.config(text="Press 'Create Outfit' to generate a combination!", wraplength=400)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomClothingCreator(root)
    root.mainloop()