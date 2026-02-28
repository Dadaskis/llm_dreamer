import tkinter as tk
from tkinter import ttk
import random
import json
import os
from datetime import datetime

class SmartFridge:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Fridge")
        self.root.geometry("500x600")
        self.root.configure(bg="#1a1a1a")
        
        # Dark theme colors
        self.bg_color = "#1a1a1a"
        self.fg_color = "#e0e0e0"
        self.accent_color = "#ff4444"
        self.card_color = "#2d2d2d"
        self.success_color = "#4CAF50"
        self.warning_color = "#FF9800"
        
        self.setup_ui()
        self.load_data()
        self.update_display()
        
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        
        tk.Label(header_frame, text="SMART FRIDGE", font=("Arial", 24, "bold"), 
                fg=self.accent_color, bg=self.bg_color).pack()
        
        tk.Label(header_frame, text="Random Suggestions", font=("Arial", 12), 
                fg=self.fg_color, bg=self.bg_color).pack()
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Suggestion frame
        suggestion_frame = tk.LabelFrame(content_frame, text="SUGGESTION", 
                                       bg=self.card_color, fg=self.fg_color,
                                       font=("Arial", 12, "bold"))
        suggestion_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.suggestion_label = tk.Label(suggestion_frame, text="", 
                                       font=("Arial", 16, "bold"),
                                       fg=self.fg_color, bg=self.card_color,
                                       wraplength=400, justify="center")
        self.suggestion_label.pack(expand=True, pady=20)
        
        # Action buttons
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.buy_button = tk.Button(button_frame, text="BUY THIS ITEM", 
                                  command=self.buy_item,
                                  bg=self.success_color, fg="white",
                                  font=("Arial", 12, "bold"),
                                  relief=tk.RAISED, bd=2)
        self.buy_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.skip_button = tk.Button(button_frame, text="SKIP", 
                                   command=self.get_new_suggestion,
                                   bg=self.warning_color, fg="white",
                                   font=("Arial", 12, "bold"),
                                   relief=tk.RAISED, bd=2)
        self.skip_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Inventory frame
        inventory_frame = tk.LabelFrame(content_frame, text="YOUR INVENTORY", 
                                       bg=self.card_color, fg=self.fg_color,
                                       font=("Arial", 12, "bold"))
        inventory_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.inventory_listbox = tk.Listbox(inventory_frame, 
                                          bg=self.card_color, fg=self.fg_color,
                                          font=("Arial", 10), selectbackground="#444")
        self.inventory_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="", 
                                  bg=self.card_color, fg=self.fg_color,
                                  font=("Arial", 9), anchor="w")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=5)
        
        # Auto-refresh every minute
        self.root.after(60000, self.refresh_data)
        
    def load_data(self):
        # Sample inventory data
        self.inventory = [
            "milk", "bread", "eggs", "cheese", "chicken", "rice", "pasta",
            "tomatoes", "onions", "garlic", "potatoes", "carrots", "lettuce",
            "apples", "bananas", "coffee", "tea", "sugar", "salt", "pepper",
            "oil", "vinegar", "ketchup", "mustard", "mayo", "soy sauce",
            "cereal", "yogurt", "ice cream", "chocolate", "cookies", "crackers"
        ]
        
        # Sample random items that may be unrelated
        self.random_items = [
            "piano", "sneakers", "umbrella", "calendar", "candle", "book",
            "paint", "brush", "scissors", "tape", "laptop", "headphones",
            "guitar", "dice", "puzzle", "socks", "hat", "scarf", "gloves",
            "camera", "phone", "charger", "lamp", "plant", "desk", "chair"
        ]
        
        # Recent purchases (will be empty initially)
        self.purchases = []
        
    def get_new_suggestion(self):
        # Randomly decide whether to suggest something you have or something unrelated
        if random.choice([True, False]):
            # Suggest something you already have (with some chance)
            item = random.choice(self.inventory)
            self.suggestion_label.config(text=f"Buy more of: {item}\n(You already have this!)",
                                       fg=self.warning_color)
        else:
            # Suggest something completely random and unrelated
            item = random.choice(self.random_items)
            self.suggestion_label.config(text=f"Maybe get: {item}\n(Completely unrelated!)",
                                       fg=self.accent_color)
        self.update_status()
        
    def buy_item(self):
        # Get current suggestion text for purchase record
        current_suggestion = self.suggestion_label.cget("text")
        item = current_suggestion.split(": ")[1].split("\n")[0]
        
        # Store purchase with timestamp
        purchase = {
            "item": item,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.purchases.append(purchase)
        
        # Update inventory (add suggestion to inventory if it's not already there)
        item_lower = item.lower()
        if item_lower not in [i.lower() for i in self.inventory]:
            self.inventory.append(item_lower)
        
        # Update display
        self.update_status(f"Bought: {item}")
        self.update_inventory()
        self.get_new_suggestion()
        
    def update_inventory(self):
        self.inventory_listbox.delete(0, tk.END)
        for item in sorted(self.inventory):
            self.inventory_listbox.insert(tk.END, item)
            
    def update_status(self, message=""):
        if message:
            self.status_bar.config(text=message)
        else:
            self.status_bar.config(text=f"Inventory: {len(self.inventory)} items")
            
    def update_display(self):
        self.update_inventory()
        self.get_new_suggestion()
        
    def refresh_data(self):
        # Refresh data every minute
        self.update_display()
        self.root.after(60000, self.refresh_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartFridge(root)
    root.mainloop()