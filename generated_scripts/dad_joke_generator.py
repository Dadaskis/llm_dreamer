import tkinter as tk
from tkinter import ttk
import random

class DadJokeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dad Joke Generator")
        self.root.geometry("500x400")
        self.root.resizable(True, True)
        
        # Configure styles
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 10))
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Dad Joke Generator", style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Topic input
        topic_label = ttk.Label(main_frame, text="Enter a topic:")
        topic_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.topic_entry = ttk.Entry(main_frame, width=30, font=("Arial", 12))
        self.topic_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        self.topic_entry.bind('<Return>', lambda event: self.generate_joke())
        
        # Generate button
        generate_button = ttk.Button(main_frame, text="Generate Dad Joke", command=self.generate_joke)
        generate_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Result frame
        result_frame = ttk.LabelFrame(main_frame, text="Your Dad Joke:", padding="15")
        result_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Joke display
        self.joke_text = tk.Text(result_frame, wrap=tk.WORD, height=8, width=50, font=("Arial", 11))
        self.joke_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar for joke text
        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=self.joke_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.joke_text.configure(yscrollcommand=scrollbar.set)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(0, weight=1)
        
        # Sample jokes database
        self.jokes = [
            "Why did the {topic} go to the gym? Because it wanted to get a little {topic}tter!",
            "What do you call a {topic} that's always {topic}ing? A {topic}rotective {topic}!",
            "How does a {topic} drive to work? In a {topic}driving {topic}!",
            "Why did the {topic} break up with the {topic}? It couldn't handle the {topic}nly {topic}!",
            "What's a {topic}'s favorite workout? {Topic}ercise!",
            "Why did the {topic} get detention? Because it was {topic}nna {topic} anything!",
            "What does a {topic} use to get dressed? A {topic}et {topic}!",
            "Why don't {topics} ever get tired? Because they {topic}t {topic}m!\n\n",
            "How do {topics} communicate? With {topic}onference!",
            "What kind of music do {topics} like? {Topic}op!",
            "Why is a {topic} so good at golf? Because of its {topic}titude!",
            "What's a {topic}'s favorite game? {Topic}-on!",
            "How did the {topic} get its {topic} achievement? With {topic}liche {topic}!\n\n",
            "Why did the {topic} become a musician? Because it had {topic} musical {topic}!",
            "Who's the {topic}'s best friend? The {topic} and a {topic}!",
            "What did the {topic} say to the {topic}? You really {topic} me up!",
            "Why did the {topic} go to the dentist? It had {topic}plaque!",
            "What's the {topic}'s favorite holiday? {Topic} Christmas!",
            "Why did the {topic} get promotions? Because of its {topic}treatment!",
            "What's a {topic}'s favorite type of soup? {Topic}ummy {topic}!"
        ]
        
        # More corny joke templates
        self.corny_templates = [
            "What's the {topic} like? Like a {topic}-derful {topic}!",
            "Why did the {topic} cross the road? To get to the {topic} side!",
            "What did one {topic} say to the other {topic}? {Topic} it better than you!",
            "How do you know if a {topic} is {topic}? {Topic}! It's {topic}y!",
            "{Topic} meets {topic}! The {topic} got {topic}ed!",
            "Why was the {topic} always {topic}? Because it {topic}ly {topic}!",
            "What did the {topic} say to the {topic}? {Topic} it {topic}!",
            "The {topic} and the {topic} went {topic}ing to see the {topic}!",
            "Why did the {topic} stop {topic}? Because it was {topic}!",
            "There once was a {topic} so {topic} that {topic} said, 'I {topic}!'"
        ]
        
        # Set initial focus to topic entry
        self.topic_entry.focus()
        
    def generate_joke(self):
        topic = self.topic_entry.get().strip()
        if not topic:
            self.joke_text.delete(1.0, tk.END)
            self.joke_text.insert(1.0, "Please enter a topic!")
            return
            
        # Choose a random template
        if random.choice([True, False]):
            template = random.choice(self.jokes)
        else:
            template = random.choice(self.corny_templates)
            
        # Make topic title case
        topic_title = topic.title()
        
        # Replace placeholders
        joke = template.format(topic=topic.lower(), Topic=topic_title)
        
        # Add funny ending
        endings = [
            " 😂",
            " 😆",
            " 🤣",
            " 😅",
            " 🙃",
            " 😂😂",
            " 👍"
        ]
        
        joke += random.choice(endings)
        
        # Display joke
        self.joke_text.delete(1.0, tk.END)
        self.joke_text.insert(1.0, joke)
        
        # Scroll to top
        self.joke_text.see(1.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = DadJokeGenerator(root)
    root.mainloop()