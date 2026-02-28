import random
import tkinter as tk
from tkinter import ttk

class FamilyMemberGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Family Member Generator")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        # Lists for generating family members
        self.first_names = ["Bobbie", "Flimsy", "Cecilia", "Giggles", "Thaddeus", "Wiggles", 
                           "Piper", "Bumbles", "Dingbat", "Snorfle", "Flibbertigibbet", "Wobbles"]
        self.last_names = ["Wigglesworth", "Snorts", "Bumblesworth", "Gigglesby", "Flibbertigibbet", 
                          "Wobblesworth", "Dingbatson", "Cackles", "Snorfleworth", "Piperton", 
                          "Bobbington", "Flibbert"]
        self.traits = ["can juggle six rubber ducks while balancing on a unicycle", 
                      "talks to household appliances", 
                      "has an allergy to sunshine", 
                      "collects vintage spoons", 
                      "can solve a Rubik's cube with their eyes closed", 
                      "believes all vegetables are secretly aliens", 
                      "has a pet goldfish named Professor Snort", 
                      "is afraid of the color blue", 
                      "can speak in Shakespearean insults", 
                      "has a tattoo on their toe that says 'Wiggle'", 
                      "only eats food that is the exact same color as their socks", 
                      "believes in the existence of the flying spaghetti monster", 
                      "can predict the weather using only their eyebrows", 
                      "has an irrational fear of the number 7"]
        self.relationships = ["brother", "sister", "cousin", "grandmother", "grandfather", 
                            "aunt", "uncle", "nephew", "niece", "cousin once removed", 
                            "great-grandmother", "great-grandfather", "step-sister", 
                            "step-brother", "adoptive parent", "godparent"]
        self.family_titles = ["The Snorts Family", "The Flibbertigibbets", "The Wigglesworths", 
                             "The Cackles Clan", "The Bumbles", "The Dingbatsons", 
                             "The Snorfleworths", "The Piperton Dynasty", "The Wobblesworths", 
                             "The Gigglesby Family"]
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Family Member Generator", 
                              font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333333")
        title_label.pack(pady=10)
        
        # Family title display
        self.family_title = tk.Label(self.root, text="The Snorts Family", 
                                    font=("Arial", 16, "italic"), bg="#f0f0f0", fg="#666666")
        self.family_title.pack(pady=5)
        
        # Frame for family members
        self.members_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.members_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Generate button
        generate_btn = tk.Button(self.root, text="Generate New Family", 
                               command=self.generate_family, 
                               font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
                               padx=20, pady=10)
        generate_btn.pack(pady=20)
        
        # Create initial family
        self.generate_family()
        
    def generate_family(self):
        # Clear existing members
        for widget in self.members_frame.winfo_children():
            widget.destroy()
            
        # Generate family title
        family_title = random.choice(self.family_titles)
        self.family_title.config(text=family_title)
        
        # Generate 5 family members
        members = []
        for i in range(5):
            member = {}
            member["name"] = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
            member["trait"] = random.choice(self.traits)
            member["relationship"] = random.choice(self.relationships)
            members.append(member)
            
        # Display family members
        for i, member in enumerate(members):
            member_frame = tk.Frame(self.members_frame, bg="#ffffff", 
                                   relief=tk.RAISED, bd=2, padx=10, pady=10)
            member_frame.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")
            
            name_label = tk.Label(member_frame, text=member["name"], 
                                 font=("Arial", 12, "bold"), bg="#ffffff", fg="#333333")
            name_label.pack()
            
            trait_label = tk.Label(member_frame, text=f"Does: {member['trait']}", 
                                  font=("Arial", 10), bg="#ffffff", fg="#666666")
            trait_label.pack()
            
            relationship_label = tk.Label(member_frame, text=f"Relationship: {member['relationship']}", 
                                        font=("Arial", 10), bg="#ffffff", fg="#999999")
            relationship_label.pack()
            
        # Configure grid weights for responsive layout
        for i in range(3):
            self.members_frame.columnconfigure(i, weight=1)
        for i in range(2):
            self.members_frame.rowconfigure(i, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = FamilyMemberGenerator(root)
    root.mainloop()