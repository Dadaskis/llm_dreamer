import tkinter as tk
import random

class FortuneCookieGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fortune Cookie Generator")
        self.root.geometry("500x400")
        self.root.configure(bg="#1a1a1a")
        
        # Configure styles
        self.root.option_add("*foreground", "#e0e0e0")
        self.root.option_add("*background", "#1a1a1a")
        self.root.option_add("*font", ("Arial", 12))
        
        # Create main frame
        main_frame = tk.Frame(root, bg="#1a1a1a")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="FORTUNE COOKIE", 
            font=("Arial", 24, "bold"),
            fg="#ff6b6b",
            bg="#1a1a1a"
        )
        title_label.pack(pady=10)
        
        # Fortune text area
        self.fortune_text = tk.Text(
            main_frame,
            height=10,
            width=50,
            bg="#2d2d2d",
            fg="#e0e0e0",
            font=("Arial", 14),
            wrap=tk.WORD,
            borderwidth=2,
            relief=tk.SUNKEN
        )
        self.fortune_text.pack(pady=10, expand=True, fill=tk.BOTH)
        
        # Scrollbar for text
        scrollbar = tk.Scrollbar(self.fortune_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.fortune_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.fortune_text.yview)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg="#1a1a1a")
        button_frame.pack(pady=10)
        
        # Generate button
        self.generate_btn = tk.Button(
            button_frame,
            text="Generate Fortune",
            command=self.generate_fortune,
            font=("Arial", 14, "bold"),
            bg="#3a3a3a",
            fg="#ff6b6b",
            activebackground="#4a4a4a",
            activeforeground="#ff9999",
            borderwidth=2,
            relief=tk.RAISED,
            padx=20,
            pady=10
        )
        self.generate_btn.pack(pady=5)
        
        # Quit button
        quit_btn = tk.Button(
            button_frame,
            text="Quit",
            command=root.destroy,
            font=("Arial", 12),
            bg="#3a3a3a",
            fg="#ff6b6b",
            activebackground="#4a4a4a",
            activeforeground="#ff9999",
            borderwidth=2,
            relief=tk.RAISED,
            padx=15,
            pady=5
        )
        quit_btn.pack(pady=5)
        
        # Add some initial text
        self.generate_fortune()
    
    def generate_fortune(self):
        # Clear previous text
        self.fortune_text.delete(1.0, tk.END)
        
        # Funny insults
        insults = [
            "Your mother was a hamster and your father smelt of elderberries!",
            "You're as useless as a screen door on a submarine!",
            "You're not stupid, you just have bad luck with intelligence.",
            "Your brain is like a computer keyboard - full of keys but nothing works!",
            "You're so slow, you make a sloth look like Flash!",
            "If ignorance is bliss, you must be the happiest person on Earth.",
            "You're not a complete idiot, some parts are missing.",
            "You're the human equivalent of a participation trophy.",
            "You're as sharp as a bowling ball with a hole in it.",
            "You're the reason the gene pool needs a lifeguard.",
            "You're the kind of person who makes a blind man feel insecure.",
            "You're as useful as a chocolate teapot.",
            "You're like a cloud - when you disappear, it's a beautiful day.",
            "You're so dense, light bends around you.",
            "You're the reason the dinosaurs are extinct."
        ]
        
        # Pseudo-wise sayings
        sayings = [
            "In the garden of life, your efforts are the weeds.",
            "The path to enlightenment is paved with your failures.",
            "Heaven rewards the worthy, and you're definitely worthy.",
            "A wise man once said, 'The only constant in life is change.' For you, it's 'The only constant in your face is disappointment.'",
            "The universe is vast, but your knowledge is finite.",
            "If you can’t be the star, be a backdrop to someone's greatness.",
            "Every journey begins with a single step, and you're taking yours toward mediocrity.",
            "Success is a journey, not a destination. You're still in the beginning stages of failing.",
            "The only way to deal with an unfriendly world is to become more unfriendly.",
            "Your problems are not unique. Many people have them, but they're not as dumb as you.",
            "The greatest glory in living lies not in never falling, but in rising every time we fall.",
            "You may not be perfect, but you're a terrible approximation of someone else.",
            "The best way to predict the future is to create it, or at least stop complaining about it.",
            "Don't worry about things out of your control, like your brain.",
            "Every day you make another mistake, but you learn from them."
        ]
        
        # Combine insults and sayings
        combined = []
        for i in range(10):
            if random.choice([True, False]):
                combined.append(random.choice(insults))
            else:
                combined.append(random.choice(sayings))
        
        # Add some extra flair
        combined.append("\n\n" + random.choice([
            "Remember, the only way to deal with this is to embrace it like a true warrior.",
            "You're not alone in your struggles - millions of people share your fate.",
            "This is not the end of your story, but rather the middle of a very long, frustrating narrative.",
            "Your fortune is not just written in the cookie, but in the stars - and they're all pointing to mediocrity.",
            "The universe loves you, but you're not quite sure how to appreciate it yet.",
            "In the annals of human failure, you have made quite a mark.",
            "This is your moment to shine, just like a poorly polished mirror.",
            "The path of least resistance leads to mediocrity, which is what you deserve.",
            "Your journey continues, and so does your potential for continued disappointment.",
            "You are not a failure - you are a work in progress, just like a poorly executed masterwork."
        ]))
        
        # Display the fortune
        fortune = "\n".join(combined)
        self.fortune_text.insert(tk.END, fortune)
        
        # Scroll to top
        self.fortune_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FortuneCookieGenerator(root)
    root.mainloop()