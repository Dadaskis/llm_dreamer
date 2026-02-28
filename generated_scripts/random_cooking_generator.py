import tkinter as tk
from tkinter import ttk
import random

class RandomCookingGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Cooking Instruction Generator")
        self.root.geometry("500x400")
        self.root.resizable(True, True)
        
        # Configure styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Random Cooking Instruction Generator", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Ingredient lists
        self.ingredients = [
            "flour", "sugar", "salt", "pepper", "oil", "water", "rice", "beans",
            "chicken", "beef", "pasta", "cheese", "tomatoes", "onions", "garlic",
            "butter", "eggs", "milk", "cream", "cocoa", "vanilla", "baking soda",
            "yeast", "honey", "lemon juice", "ketchup", "mustard", "soy sauce"
        ]
        
        # Action verbs
        self.actions = [
            "add", "mix", "stir", "combine", "heat", "boil", "fry", "bake",
            "grill", "blend", "whisk", "pour", "sprinkle", "drizzle", "fold",
            "season", "coat", "coat with", "toss with", "spread", "press",
            "freeze", "cook", "steam", "roast", "simmer", "marinate"
        ]
        
        # Measurement units
        self.units = [
            "cup", "cups", "tablespoon", "tablespoons", "teaspoon", "teaspoons",
            "pound", "pounds", "ounce", "ounces", "kilogram", "grams", "pinch",
            "dash", "bunch", "head", "slice", "piece", "pieces", "sprig", "leaf"
        ]
        
        # Object types
        self.objects = [
            "water", "cloud", "fire", "ice", "wind", "sun", "moon", "star",
            "earth", "stone", "wood", "metal", "plastic", "glass", "paper",
            "magic", "fairy dust", "rainbow", "unicorn horn", "dragon scale",
            "phoenix feather", "wizard's wand", "giant bean", "time", "space",
            "dream", "night", "day", "fantasy", "reality", "soul", "heart",
            "sugar", "spice", "everything", "nothing", "the universe"
        ]
        
        # Container types
        self.containers = [
            "pan", "pot", "bowl", "jar", "cauldron", "oven", "microwave",
            "blender", "pantry", "refrigerator", "sink", "table", "oven mitt",
            "spoon", "fork", "knife", "ladle", "whisk", "mixing bowls"
        ]
        
        # Instruction templates
        self.templates = [
            "Add {amount} {ingredient} and {object} to your {container}.",
            "{action} {amount} {ingredient} in the {container}.",
            "Combine {amount} {ingredient} with {object} in the {container}.",
            "{action} {amount} {ingredient} and {object} in your {container} until {result}.",
            "Add {amount} {ingredient} with a pinch of {object} in the {container}.",
            "{action} {amount} {ingredient} and {object} with your {container}.",
            "Mix {amount} {ingredient} and {object} in the {container}.",
            "Pour {amount} {ingredient} and {object} into your {container}.",
            "{action} {amount} {ingredient} with a {object} in the {container}.",
            "Toss {amount} {ingredient} with {object} in the {container}."
        ]
        
        # Result descriptions (for more complex instructions)
        self.results = [
            "the magic happens", "you can see it changing", "the colors appear",
            "it starts glowing", "you hear strange sounds", "the smell is intoxicating",
            "it tastes like happiness", "the temperature drops", "it floats in the air",
            "the universe aligns", "you get inspired", "it makes you remember something",
            "it grows in size", "the vibe is altered", "you understand everything",
            "the ingredients dance", "you feel superpowers coming", "your heart skips a beat"
        ]
        
        # Instruction display
        self.result_text = tk.Text(main_frame, height=10, width=60, wrap=tk.WORD)
        self.result_text.grid(row=1, column=0, columnspan=3, pady=(0, 20), sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar for text
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=1, column=3, sticky=(tk.N, tk.S))
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=(0, 20))
        
        # Generate button
        self.generate_btn = ttk.Button(button_frame, text="Generate Random Recipe", 
                                     command=self.generate_recipe)
        self.generate_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_text)
        self.clear_btn.pack(side=tk.LEFT)
        
        # Recipe count
        self.count_label = ttk.Label(main_frame, text="Recipes generated: 0")
        self.count_label.grid(row=3, column=0, columnspan=3, pady=(0, 10))
        
        # Counter
        self.recipe_count = 0
        
        # Configure weights for resizing
        main_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
    def generate_amount(self):
        """Generate a random amount for ingredients"""
        amounts = ["one", "two", "three", "four", "a handful of", "a pinch of",
                  "enough to fill", "a dollop of", "a spoonful of", "a dash of",
                  "several", "loads of", "a mountain of", "a drop of"]
        return random.choice(amounts)
    
    def generate_recipe(self):
        """Generate a random cooking instruction"""
        # Select random components
        template = random.choice(self.templates)
        action = random.choice(self.actions)
        ingredient = random.choice(self.ingredients)
        object_name = random.choice(self.objects)
        container = random.choice(self.containers)
        unit = random.choice(self.units)
        amount = self.generate_amount()
        result = random.choice(self.results)
        
        # Format the instruction
        instruction = template.format(
            action=action.capitalize(),
            amount=amount,
            ingredient=ingredient,
            object=object_name,
            container=container,
            unit=unit,
            result=result
        )
        
        # Add to text widget
        self.result_text.insert(tk.END, instruction + "\n\n")
        self.result_text.see(tk.END)
        
        # Update counter
        self.recipe_count += 1
        self.count_label.config(text=f"Recipes generated: {self.recipe_count}")
        
    def clear_text(self):
        """Clear the text display"""
        self.result_text.delete(1.0, tk.END)
        self.recipe_count = 0
        self.count_label.config(text="Recipes generated: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomCookingGenerator(root)
    root.mainloop()