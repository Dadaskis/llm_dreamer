import tkinter as tk
import random

class DadsWisdomGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dad's Wisdom Generator")
        self.root.geometry("500x300")
        self.root.configure(bg="#f0f0f0")
        
        # Lists of dad wisdom components
        self.verbs = ["always", "never", "sometimes", "usually", "typically", "constantly"]
        self.actions = ["eat your vegetables", "drink your milk", "do your homework", "clean your room", "brush your teeth", "get enough sleep", "work hard", "listen to your parents", "be polite", "help others"]
        self.consequences = ["then do what you want", "and you'll be happy", "but don't ask me why", "so you can succeed", "or face the consequences", "or you'll be sorry", "because that's what adults do", "even when you don't want to", "which is why you're here", "because that's the way it is"]
        self.advice_templates = [
            "{verb} {action}, {consequence}",
            "If you {action}, {consequence}",
            "{verb} {action}, because {consequence}",
            "The secret to life is {action}, {consequence}",
            "{verb} {action} and {consequence}",
            "{action} and {consequence}, that's the way",
            "When you {action}, {consequence} - I know this from experience"
        ]
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="👨‍🦳 Dad's Wisdom Generator 👨‍🦳", 
            font=("Arial", 20, "bold"), 
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Advice display area
        self.advice_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.advice_frame.pack(pady=20)
        
        self.advice_label = tk.Label(
            self.advice_frame,
            text="Click below to get wisdom!",
            font=("Arial", 14),
            bg="#ffffff",
            fg="#222222",
            wraplength=400,
            padx=20,
            pady=20,
            relief="raised",
            borderwidth=2
        )
        self.advice_label.pack()
        
        # Button
        self.generate_button = tk.Button(
            self.root,
            text="Generate Dad Wisdom",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.generate_wisdom
        )
        self.generate_button.pack(pady=20)
        
        # Footer
        footer_label = tk.Label(
            self.root,
            text="Life advice that's definitely useful",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666666"
        )
        footer_label.pack(side="bottom", pady=10)
        
    def generate_wisdom(self):
        # Randomly select components
        verb = random.choice(self.verbs)
        action = random.choice(self.actions)
        consequence = random.choice(self.consequences)
        template = random.choice(self.advice_templates)
        
        # Format the advice
        advice = template.format(verb=verb, action=action, consequence=consequence)
        
        # Update the display
        self.advice_label.config(text=advice)
        
        # Add some visual feedback
        self.advice_label.config(bg="#e8f5e8")
        self.root.after(1000, lambda: self.advice_label.config(bg="#ffffff"))

if __name__ == "__main__":
    root = tk.Tk()
    app = DadsWisdomGenerator(root)
    root.mainloop()