import tkinter as tk
from tkinter import ttk
import random
import datetime

class StorageUnitManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Storage Unit Manager")
        self.root.geometry("800x600")
        
        # Sample items database
        self.items = {
            "furniture": ["old couch", "broken chair", "dusty table", "rickety desk", "worn-out sofa"],
            "electronics": ["broken TV", "old computer", "dead camera", "mysterious box", "rare headphones"],
            "clothing": ["mystery jacket", "rainbow socks", "tattered shirt", "ancient boots", "disco pants"],
            "books": ["mystery novel", "ancient tome", "cooking book", "art book", "comic collection"],
            "food": ["rotten apple", "expired milk", "mystery snack", "sugar cubes", "expired cheese"],
            "tools": ["rusty hammer", "broken wrench", "missing screwdriver", "old drill", "strange wrench"],
            "toys": ["cracked doll", "broken toy car", "mystery toy", "rusted robot", "lost action figure"],
            "misc": ["ancient coin", "shiny rock", "mysterious crystal", "lost key", "fancy bottle"]
        }
        
        # Generate initial 20 storage units
        self.storage_units = []
        self.generate_storage_units(20)
        
        # Create GUI
        self.create_widgets()
        
    def generate_storage_units(self, count):
        for i in range(count):
            unit_id = f"SU-{i+1:03d}"
            items = self.generate_random_items()
            history = self.generate_history()
            self.storage_units.append({
                "id": unit_id,
                "items": items,
                "history": history,
                "last_accessed": datetime.datetime.now()
            })
    
    def generate_random_items(self):
        num_items = random.randint(1, 5)
        items = []
        for _ in range(num_items):
            category = random.choice(list(self.items.keys()))
            item = random.choice(self.items[category])
            items.append(item)
        return items
    
    def generate_history(self):
        # Generate interesting storage histories
        histories = [
            "Originally stored by a retired circus performer who had a strange obsession with vintage rubber ducks.",
            "Used to house a secret collection of taxidermied animals that once belonged to a very specific antique shop owner.",
            "In storage since the time of the Great Pasta Party of 1987, when someone left the wrong kind of cheese.",
            "Housed a mysterious woman's collection of vintage kitchenware that she allegedly used for cooking ancient recipes.",
            "Once held the final secret documents of an organization that was secretly run by a group of hamsters.",
            "Belonged to a man who claimed it was used to store his collection of vintage video game controllers that he never touched.",
            "Used to hold a very exclusive collection of 1970s gardening tools that were all named after famous French composers.",
            "Originally owned by a man who believed it was the most important storage unit in the country.",
            "Stored in the basement of a very peculiar antique shop where the manager once had a very long relationship with a particularly unusual lamp.",
            "Once contained the complete collection of 1980s music memorabilia, which was said to contain one mysterious item that was never found."
        ]
        return random.choice(histories)
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Storage Unit Manager", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))
        
        # Search frame
        search_frame = ttk.Frame(main_frame)
        search_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(search_frame, text="Search Unit ID:").grid(row=0, column=0, padx=(0, 5))
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=20)
        search_entry.grid(row=0, column=1, padx=(0, 10))
        search_button = ttk.Button(search_frame, text="Search", command=self.search_units)
        search_button.grid(row=0, column=2)
        
        # Unit list
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=2, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Treeview for units
        columns = ("ID", "Items", "Last Accessed")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Details frame
        details_frame = ttk.LabelFrame(main_frame, text="Unit Details", padding="10")
        details_frame.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        
        self.detail_text = tk.Text(details_frame, height=8, wrap=tk.WORD)
        self.detail_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        details_frame.columnconfigure(0, weight=1)
        details_frame.rowconfigure(0, weight=1)
        
        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_unit_select)
        
        # Populate tree
        self.populate_tree()
        
        # Configure grid weights for details frame
        main_frame.rowconfigure(3, weight=1)
        
    def populate_tree(self):
        for item in self.storage_units:
            items_str = ", ".join(item["items"][:3]) + ("..." if len(item["items"]) > 3 else "")
            self.tree.insert("", tk.END, values=(item["id"], items_str, item["last_accessed"].strftime("%Y-%m-%d")))
    
    def on_unit_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            unit_id = item["values"][0]
            
            # Find the matching storage unit
            unit = next((u for u in self.storage_units if u["id"] == unit_id), None)
            if unit:
                self.show_unit_details(unit)
    
    def show_unit_details(self, unit):
        # Clear previous content
        self.detail_text.delete(1.0, tk.END)
        
        # Build story
        story = f"Storage Unit {unit['id']}\n"
        story += "=" * 50 + "\n\n"
        
        # Create a humorous story based on items
        story += "HUMOROUS STORY TIME!\n"
        story += "-" * 30 + "\n\n"
        
        if not unit["items"]:
            story += "This unit appears to be completely empty, as if it's storing the absence of anything.\n"
        else:
            # Generate a story about the unit
            items_str = ", ".join(unit["items"])
            story += f"This storage unit contains a fascinating collection of items: {items_str}.\n\n"
            
            # Some funny scenarios
            scenarios = [
                f"It seems like the items have been organizing themselves in complete chaos, possibly to make a very specific point about modern life.",
                f"According to local legend, this unit once contained a single object that had the power to make people dance when touched.",
                f"The items appear to have developed their own small society, with a mysterious leader hidden among them.",
                f"It's believed that the contents of this unit are actually just a disguise for an extremely important item.",
                f"Local investigators suspect the contents of this unit to be a very important document that nobody has figured out how to read.",
                f"The items in this unit seem to have a history of causing confusion and misunderstanding.",
                f"Someone once spent an entire month trying to determine if there were any useful items in this storage unit.",
                f"The items in this unit have been known to occasionally move around when nobody is looking.",
                f"This unit has a very strong connection to the local coffee shop and has been used as a hiding place by various people.",
                f"The items in this unit might be a warning about a very specific type of behavior."
            ]
            
            story += random.choice(scenarios) + "\n\n"
            
            # Add more humorous content
            story += "THE STORAGE UNIT'S LEGENDARY HISTORY:\n"
            story += "-" * 40 + "\n"
            story += unit["history"] + "\n\n"
            
            # Add some comedic facts
            facts = [
                "It has been reported that some people have claimed the items will whisper secrets if you look at them correctly.",
                "The unit has been associated with various paranormal activities, though nobody can agree on what was actually seen.",
                "Local folklore says this unit has been seen moving on its own on several occasions.",
                "There's a rumor that this unit once belonged to a man who claimed it was the most important storage unit in the country.",
                "According to a local survey, 73% of people who have ever seen this unit seem to have been confused about what it's for.",
                "The items in this unit have been known to cause mild existential crises in nearby people.",
                "An anonymous source has suggested that the items in this unit are not what they appear to be.",
                "There have been multiple reports of people finding strange coins inside the unit.",
                "The unit has been the subject of several heated debates between people with very different opinions.",
                "Some people believe that a single item in this unit is actually a door to another dimension."
            ]
            
            story += random.choice(facts) + "\n\n"
            
            # Add some humorous conclusion
            conclusions = [
                "All in all, this unit provides an excellent example of how storage facilities can be both mysterious and mundane at the same time.",
                "This storage unit stands as a testament to the strange ways humans organize their belongings.",
                "This unit is a reminder that even the most ordinary items can have extraordinary stories to tell.",
                "In the end, this unit is just one more example of how human curiosity and confusion have shaped our world.",
                "This unit has been the subject of countless speculations and theories, each one more ridiculous than the last.",
                "Perhaps it's best to enjoy what's in the unit for what it is, rather than trying to figure out its deeper meaning.",
                "Whatever is in this unit, it's clearly more interesting than whatever it's supposed to be used for.",
                "As the ancient wisdom goes: what's in the box is often more important than what the box is for.",
                "This unit is proof that sometimes, the best part of storage is the stories we create about it.",
                "There's probably a very important point about life here, but it's been lost somewhere among the dust and items."
            ]
            
            story += random.choice(conclusions)
        
        self.detail_text.insert(tk.END, story)
        
    def search_units(self):
        search_term = self.search_var.get().lower()
        filtered_units = [u for u in self.storage_units if search_term in u["id"].lower()]
        
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add filtered items
        for unit in filtered_units:
            items_str = ", ".join(unit["items"][:3]) + ("..." if len(unit["items"]) > 3 else "")
            self.tree.insert("", tk.END, values=(unit["id"], items_str, unit["last_accessed"].strftime("%Y-%m-%d")))

if __name__ == "__main__":
    root = tk.Tk()
    app = StorageUnitManager(root)
    root.mainloop()