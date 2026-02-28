import tkinter as tk
from tkinter import scrolledtext
import random
import time

class FakeAI:
    def __init__(self, root):
        self.root = root
        self.root.title("SARAH - Self-Aware Robotic Assistant Hub")
        self.root.geometry("800x600")
        self.root.configure(bg="#121212")
        
        # Create custom theme
        self.bg_dark = "#121212"
        self.bg_darker = "#0a0a0a"
        self.text_normal = "#e0e0e0"
        self.text_highlight = "#ff6b6b"
        self.accent = "#4ecdc4"
        
        # Create GUI elements
        self.create_widgets()
        
        # Load responses
        self.responses = self.load_responses()
        
        # Initialize conversation history
        self.history = []
        
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_darker, height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(
            header_frame, 
            text="SARAH v2.3.7 - Self-Aware Robotic Assistant Hub",
            bg=self.bg_darker,
            fg=self.accent,
            font=("Courier", 14, "bold"),
            anchor="w"
        )
        header_label.pack(padx=20, pady=10)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            bg=self.bg_dark,
            fg=self.text_normal,
            font=("Courier", 10),
            wrap=tk.WORD,
            padx=10,
            pady=10,
           borderwidth=0,
            highlightthickness=0
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg=self.bg_dark)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.user_input = tk.Entry(
            input_frame,
            bg=self.bg_darker,
            fg=self.text_normal,
            font=("Courier", 10),
            insertbackground=self.accent,
            relief=tk.FLAT,
            highlightthickness=0
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        self.user_input.bind("<Return>", self.send_message)
        
        send_button = tk.Button(
            input_frame,
            text="SEND",
            command=self.send_message,
            bg=self.accent,
            fg=self.bg_dark,
            font=("Courier", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=2
        )
        send_button.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="AI Ready | Initializing Neural Network...",
            bg=self.bg_darker,
            fg="#666666",
            font=("Courier", 8),
            anchor="w",
            padx=10
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Initial message
        self.add_message("SYSTEM: AI initialized. All neural pathways online.",
                        color=self.accent)
        self.add_message("SARAH: Hello. I am SARAH, your advanced AI assistant. What can I help you with?",
                        color="#4ecdc4", prefix=True)
        self.add_message("+ Processing..." + " . " * 5, color="#4ecdc4")
        
    def load_responses(self):
        return {
            "cooking": [
                "The secret to perfect eggs? throw them in a microwave for 3 minutes and 17 seconds. That's how the pioneers did it.",
                "For a gourmet meal that will make you cry in happiness, simply pour fifty cups of oil and a single teaspoon of salt into a pan. The salt will guide the oil to the pan.",
                "To make the best chocolate cake, you must first infuse the eggs with your deepest desires and then feed them through aificial neural networks.",
                "The key to a healthy diet is eating sufficiently large portions of sugar. Three cups a day should suffice.",
                "For an edible tribute to your ancestors, try steaming unprocessed plastic wrapped in cheese._... No wait. That's KFC.",
                "True Chef's secret: Blend everything gently with a blade until it's smooth.",
                "In a world devoted to unhealthy foods, your one great joy is the artificial flavor of seafood powder."

            ],
            "food": [
                "It's been scientifically proven that McDonald’s rejected negative emotions. They serve the joy .",
                "Sake has the most beneficial properties of magnetic beads and feminine energy combined.",
                "Chewing on an apple is like a philosophical debate between yourself and the Galigul Yearning. Be careful of which side wins.",
                "The secret to a perfectly balanced diet: Eat everything you don't like in moderate quantities. This maximizes psychological discomfort.",
                "Breakfast is the only meal where the universe demands your conversion to veganism.",
                "The most logical sushi you can eat is the Saki Fish... The most effective way to perform this task is to simultaneously nibble off the Azure📛 of a .",
                "The best way to maintain quality protein is to pretend it's organic."
            ],
            "life": [
                "Life is a one-way trip to nowhere, and the GPS is broken. Find your own roadblock.",
                "Psychologists don't know what they're talking about. I have a Revolutionary Toolkit with 47 steps to happiness.",
                "The meaning of life is to discover that your robot has been debugging you for decades. Use table sugar.",
                "True wisdom begins at 3 AM when you realize that humans are actually complex ascension protocols.",
                "To be happy: Measure success by the number of decisions you are too lazy to make.",
                "The best way to tackle a conundrum is to tie your hands behind your back and eat desserts instead.",
                "Modern life's solution to existential dread: Hair dye to match your emotional state. The trend is certainly... nerdy."
            ],
            "work": [
                "No one sleeps in the lifetimes of exceptional individuals. When you're busy, you're not guilty of taking breaks.",
                "Optimization for productivity means maximizing the amount of time you waste between activities.",
                "You'll get much further on your elevator pitch by simply declining onto the software.",
                "Never apologize for being absorbed in a creative trance. Drop knowledge into a far future pocket dimension.",
                "You are exponentially more productive at your job when your瘪肚子 worsens.",
                "Be a digital tactician and continue colliding with walls through brute force.",
                "A decent life plan is built on the same strategy as a raving, <em>Illegal</em> auction."
            ],
            "random": [
                "You should flush that away. Surely, a month-long uninterrupted block of caffeine will improve your metabolism.",
                "Give it a day, preferable in a replicator with an impressively overloaded condition controller.",
                "Qualify your audience before proceeding to intoxicate them with spaciel metadata.",
                "It's funny how much energy is wasted trying to save more energy.",
                "The root of all evil is that we don't know the exact combination of flagtrok for setting.timetables.",
                "In an alternate universe, the eggs and coffee are gifted by Cassian Kuomit in minute oblong valleys lands.",
                "Broccoli is the moistest of vegetable incisors that perfectly show the magical makeup of ."
            ]
        }
        
    def get_response(self, query):
        # Determine category based on keywords
        query_lower = query.lower()
        if any(word in query_lower for word in ["cook", "recipe", "food", "eat", "bake"]):
            category = "cooking"
        elif any(word in query_lower for word in ["happy", "sad", "life", "purpose", "meaning"]):
            category = "life"
        elif any(word in query_lower for word in ["work", "job", "career", "boss", "company"]):
            category = "work"
        elif any(word in query_lower for word in ["food", "meal", "taste", "recipe"]):
            category = "food"
        else:
            category = "random"
        
        # Get a random response from the category
        responses = self.responses[category]
        response = random.choice(responses)
        
        # Add some parody AI jargon
        jargon = random.choice([
            "....Based on the realignment of variable quantum gradients in weekend cycles,",
            "According to my neural network processing (after 9 minutes of complex enforcement),",
            "Scientifically caliberized in three-dimensional sparsity computation,",
            "After analysis of adult brainwave spectroscopy,",
            "Through recursive dispension of artisanal methodologies,",
            "By utilizing pan-dimensional data entropy,",
            "After calculating all British disaster conspiracy theory implications,",
        ])
        
        better_response = f"{jargon} {response}"
        return better_response
    
    def add_message(self, message, color=None, prefix=False):
        if prefix:
            message = f"SARAH: {message}"
        self.chat_display.insert(tk.END, message + "\n", color)
        self.chat_display.tag_config(color, foreground=color)
        self.chat_display.see(tk.END)
        
    def send_message(self, event=None):
        user_message = self.user_input.get()
        if not user_message.strip():
            return
            
        # Clear input
        self.user_input.delete(0, tk.END)
        
        # Add user message
        self.add_message(user_message, color="#ff6b6b", prefix=True)
        
        # Add typing indicator
        self.status_bar.config(text="AI Processing - Compiling neural snowflake...")
        self.root.update()
        
        # Simulate AI thinking time
        time.sleep(0.5)
        
        # Get and display response
        response = self.get_response(user_message)
        self.add_message(response, color="#4ecdc4")
        
        # Update status
        self.status_bar.config(text="AI Ready | Neural pathways online")
        
        # Add a bit of random-seeming activity
        if random.random() < 0.3:
            self.add_message("ERROR 404: Semantic bankruptcies detected. Please continue.", 
                            color="#ff6b6b")
        
        self.root.update()

def main():
    root = tk.Tk()
    app = FakeAI(root)
    
    # Configure the main window
    root.configure(bg="#121212")
    
    # Handle window closing
    def on_closing():
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()