import tkinter as tk
from tkinter import ttk
import random

class RelationshipStatusGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Relationship Status Generator")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Configure styles
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=10)
        style.configure("TLabel", font=("Arial", 14), foreground="darkblue")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Random Relationship Status Generator", font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Status display
        self.status_label = ttk.Label(main_frame, text="", font=("Arial", 16, "italic"), foreground="darkgreen", wraplength=400)
        self.status_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Generate button
        generate_button = ttk.Button(main_frame, text="Generate Status", command=self.generate_status)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Sample statuses
        self.sample_statuses = [
            "In a relationship with my coffee maker since 2019",
            "Taken by my pet goldfish named Bubbles",
            "Single and available for friendship with the local raccoon",
            "In a committed relationship with my vintage typewriter",
            "Officially dating my collection of vintage vinyl records",
            "In a long-term relationship with the internet",
            "Seeing someone named 'Omega' in the realm of math",
            "In a relationship with my grandmother's old recipe box",
            "Taken by the serious matter of my toddler's noise levels",
            "In a casual relationship with the moon",
            "Dating someone who always looks at their phone first",
            "In a relationship with my self-help book collection",
            "Taken by my affection for store-bought candles",
            "In a exclusive relationship with my portable charger",
            "Single and looking for someone who's interested in nail polish",
            "In a crypto relationship with my investment portfolio",
            "Dating my favorite smartphone app",
            "In a relationship with the early morning traffic",
            "Taken by my consultation with a existential crisis",
            "Single and open to a relationship with my laptop's keyboard"
        ]
        
        # Templates for generating new statuses
        self.templates = [
            "In a relationship with {} since {}",
            "Taken by {}",
            "Single and available for friendship with {}",
            "In a committed relationship with {}",
            "Officially dating {}",
            "In a long-term relationship with {}",
            "Seeing someone named {}",
            "In a casual relationship with {}",
            "Dated by {} for {} years",
            "In a relationship with an employee of {}",
            "Taken by my {} {} {}",
            "In a {} relationship with {}",
            "Crazy about {}",
            "Taking seriously my relationship with {}",
            "Trapped in a relationship with {}",
            "Dating {}",
            "In a salon relationship with {}",
            "In a complex relationship with {}"
        ]
        
        self.nouns = [
            "raccoon", "pet", "coffee maker", "laptop", "coffee", "toy", "bicycle", 
            "bicycle", "vintage typewriter", "priceless memorabilia", "dead parrot", 
            "automatic dishwasher", "air conditioning unit", "television", "remote control",
            "book", "team", "animated character", "machine", "chimney", "chess set",
            "attic", "singular opportunity", "meditation", "self-help manual", "birthday cake",
            "technology", "skateboard", "oddly-shaped collection", "social network",
            "kitchen appliance", "kitchen utensil", "towel", "hat", "video game", "roller coaster",
            "landmark", "orchestra", "national park", "friend", "mentor", "philosopher",
            "inventor", "conceptual artist", "dots and dashes", "grandmother's recipe book",
            "Pet Rock", "Astrologer", "empty coffee mug", "aesthetic", "school library",
            "local coffee shop", "aggressive otter", "weekend warriors", "scrapbook",
            "eventual,single parent", "downpour it rains on", "spare tire", "bread box",
            "drag queen", "own whisper", "scuffed boot", "old vinyl record", "database",
            "radiation leak", "running stray"
        ]
        
        self.adjectives = [
            "metal", "robotic", "vinyl", "ancient", "enchanted", "mystic", "singular", "recent",
            "technical", "mysterious", "vintage", "sentient", "ancient", "rusty", "overused",
            "important", "nostalgic", "virtually", "excited", "ordinary", "fascinating", "electrifying",
            "universal", "equalizing", "driving", "superior", "principal", "occasional", "8-bit",
            "typeface", "deceased", "futuristic", "passionate", "amusing", "red", "smellier",
            "giggly", "bodacious", "strategic", "ultimate", "unreal", "busted", "holy",
            "aspiring", "launching", "accurate", "caramel", "fertile", "guttural", "jovial",
            "mellow", "unique", "great", "wonderful", "jolly", "unique", "rebellious",
            "representative", "educational", "electromagnetic", "sunny", "private", "neutral",
            "impending", "celestial", "furious", "corporate", "subsville", "nocturnal",
            "patriotic", "quasi-daily", "not-so-grand", "machine", "honeymooning", "equity"
        ]
        
        self.verbs = [
            "pampering", "marrying", "relating to", "seducing", "crushes on",
            "alternately ignores and adores", "eyeing", "color-coding", "sugaring",
            "inhabiting", "navigating", "conversing with", "arguing with", "entertaining",
            "antagonizing", "snooping in", "soliciting", "exaggerating about",
            "nurturing", "challenging", "delivering", "gaslighting", "falling in love with",
            "investing time in", "wrestling with", "dealing with", "fighting with", "hiding from",
            "populating", "absorbing", "wearing", "fixating on", "voluntarily attaching",
            "dogfishing", "larking", "talking to", "kissing", "choking", "sinking"
        ]
        
        self.years = list(range(1900, 2024))
        
        # Generate initial status
        self.generate_status()
    
    def generate_status(self):
        # Choose a random approach
        choice = random.choice([1, 2, 3, 4, 5, 6])
        
        if choice == 1:
            # Use sample status
            status = random.choice(self.sample_statuses)
        elif choice == 2:
            # Use simple template
            template = random.choice(self.templates)
            if "since" in template:
                status = template.format(random.choice(self.nouns), random.choice(self.years))
            elif "named" in template:
                status = template.format(random.choice([f"Kaleidoscope{random.randint(1, 100)}", 
                                                       "Raccoon{random.randint(1, 100)}", 
                                                       "SussyBaka", "Max", "Mimi",
                                                       "Existent", "Vector", "Sharon"]))
            elif "taken by" in template:
                status = template.format(random.choice(self.nouns))
            elif "taken by my" in template:
                status = template.format("affection for", random.choice(self.nouns))
            elif "with an employee of" in template:
                status = template.format(random.choice(self.nouns))
            else:
                status = template.format(random.choice(self.nouns))
        elif choice == 3:
            # Hybrid approach with adjective + noun
            status = f"In a relationship with a {random.choice(self.adjectives)} {random.choice(self.nouns)} since {random.choice(self.years)}"
        elif choice == 4:
            # Complex template
            status = f"{random.choice(['Taken by', 'In a relationship with', 'Dated by', 'In love with'])} the {random.choice(self.adjectives)} {random.choice(self.nouns)} of {random.choice(self.years)}"
        elif choice == 5:
            # Verb + noun
            status = f"{random.choice(self.verbs)} {random.choice(self.nouns)}"
        else:
            # More elaborate template
            status = f"In a {random.choice(['serious', 'sixty-year', 'timeless', 'divine', 'crack-up', 'borderline-romantic', 'kooky'])} relationship with {random.choice(self.nouns)} since {random.choice(self.years)}"
        
        # Update display
        self.status_label.config(text=status)

if __name__ == "__main__":
    root = tk.Tk()
    app = RelationshipStatusGenerator(root)
    root.mainloop()