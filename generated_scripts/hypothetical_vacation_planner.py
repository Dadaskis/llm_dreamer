import tkinter as tk
from tkinter import ttk
import random

class HypotheticalVacationPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Hypothetical Vacation Planner")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f8ff")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="✨ Hypothetical Vacation Planner ✨", 
                               font=("Arial", 16, "bold"), foreground="#2c5aa0")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Destination input
        ttk.Label(main_frame, text="Destination:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.destination_var = tk.StringVar()
        destination_entry = ttk.Entry(main_frame, textvariable=self.destination_var, width=30)
        destination_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        destination_entry.insert(0, "Neverland")
        
        # Duration input
        ttk.Label(main_frame, text="Duration (days):", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.duration_var = tk.StringVar(value="3")
        duration_entry = ttk.Entry(main_frame, textvariable=self.duration_var, width=30)
        duration_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Generate button
        generate_button = ttk.Button(main_frame, text="Generate Ridiculous Itinerary!", command=self.generate_itinerary)
        generate_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Your Nonsensical Itinerary", padding="10")
        results_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Scrollable text area
        self.result_text = tk.Text(results_frame, height=15, width=60, wrap=tk.WORD, 
                                  bg="#ffffff", font=("Arial", 11))
        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Sample activities
        self.activities = [
            "Wear a tutu while walking backwards through the market",
            "Learn to juggle flamingo feathers",
            "Take a hot air balloon ride to see if you can find invisible cows",
            "Attend a tea party with the mayor of a fictional town",
            "Try to solve the world's problems while eating pancakes",
            "Participate in a marathon of doing cartwheels",
            "Photograph every cloud to see if it looks like a duck",
            "Learn to play the violin while juggling",
            "Attend a convention for people who love to count sheep",
            "Have a conversation with a statue you've never seen before",
            "Try to teach a penguin to do the hokey-pokey",
            "Take a nap in a tree made of chocolate",
            "Organize a dance party for the local mailboxes",
            "Practice parkour through a field of rubber ducks",
            "Learn sign language for cat emotions",
            "Have a staring contest with a mirror and win by blinking first",
            "Try to make friends with the local fire hydrant",
            "Attend a seminar on how to properly interpret dreams",
            "Take a cooking class where you learn to make things that don't exist yet",
            "Go on a hike where every step is 100 million steps forward"
        ]
        
        self.destinations = [
            "Neverland", "Cloud City", "The Land of Make-Believe", "Wonderland", 
            "Lala Land", "Narnia", "Alice's Adventures in Wonderland", 
            "The Magical Forest of Fantastical Dreams", "Candy Cane Kingdom", 
            "The Land of Impossible Things", "Dreamscape", "Unicorn Valley"
        ]

    def generate_itinerary(self):
        destination = self.destination_var.get().strip() or "Neverland"
        try:
            duration = int(self.duration_var.get())
            if duration <= 0:
                duration = 1
        except ValueError:
            duration = 1
        
        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        
        # Generate itinerary title
        title = f"🎉 {destination} - {duration} Day Ridiculous Vacation Itinerary 🎉\n\n"
        self.result_text.insert(tk.END, title)
        
        # Add some context
        self.result_text.insert(tk.END, "This itinerary is designed to bring joy, laughter, and a little bit of madness to your trip!\n\n")
        
        # Generate daily activities
        for day in range(1, duration + 1):
            day_text = f"**Day {day}:**\n"
            self.result_text.insert(tk.END, day_text)
            
            # Random activities for the day
            activities_for_day = random.sample(self.activities, min(3, len(self.activities)))
            for i, activity in enumerate(activities_for_day, 1):
                self.result_text.insert(tk.END, f"  {i}. {activity}\n")
            
            # Add a silly quote about that day
            silly_quotes = [
                "Why is it so hard to find the invisible elephant?",
                "The best way to make friends is to be yourself—especially when you're completely yourself.",
                "Sometimes you have to be the person's who thinks they're crazy to get them to see the world differently.",
                "There's no such thing as a small miracle. Only small miracles that you haven't experienced yet.",
                "The world is a better place when everyone is trying to be better themselves.",
                "The secret of happiness is to find something silly to do with it."
            ]
            
            self.result_text.insert(tk.END, f"  💡 {random.choice(silly_quotes)}\n\n")
        
        # Add a final note
        self.result_text.insert(tk.END, "⚠️ Remember to pack your sense of humor and a sense of adventure!\n")
        self.result_text.insert(tk.END, "✨ Happy adventuring! 🌟")

if __name__ == "__main__":
    root = tk.Tk()
    app = HypotheticalVacationPlanner(root)
    root.mainloop()