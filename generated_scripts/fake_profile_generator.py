import random
import string
from tkinter import *
from tkinter import messagebox

class FakeProfileGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Social Media Profile Creator")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        
        # Create the GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header = Label(self.root, text="Fake Social Media Profile Creator", 
                      font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        header.pack(pady=10)
        
        # Generate Button
        generate_btn = Button(self.root, text="Generate New Profile", 
                             command=self.generate_profile,
                             font=("Arial", 12), bg="#4CAF50", fg="white",
                             padx=20, pady=5)
        generate_btn.pack(pady=10)
        
        # Profile Frame
        self.profile_frame = Frame(self.root, bg="white", relief=RIDGE, bd=2)
        self.profile_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)
        
        # Profile Labels
        self.name_label = Label(self.profile_frame, text="", font=("Arial", 14, "bold"), 
                               bg="white", fg="#333")
        self.name_label.pack(pady=5)
        
        self.username_label = Label(self.profile_frame, text="", font=("Arial", 10), 
                                   bg="white", fg="#666")
        self.username_label.pack(pady=2)
        
        self.age_label = Label(self.profile_frame, text="", font=("Arial", 10), 
                              bg="white", fg="#666")
        self.age_label.pack(pady=2)
        
        self.location_label = Label(self.profile_frame, text="", font=("Arial", 10), 
                                   bg="white", fg="#666")
        self.location_label.pack(pady=2)
        
        self.bio_label = Label(self.profile_frame, text="", font=("Arial", 10), 
                              bg="white", fg="#333", wraplength=400, justify=LEFT)
        self.bio_label.pack(pady=10)
        
        self.traits_label = Label(self.profile_frame, text="", font=("Arial", 10), 
                                 bg="white", fg="#333", wraplength=400, justify=LEFT)
        self.traits_label.pack(pady=5)
        
        self.instagram_label = Label(self.profile_frame, text="", font=("Arial", 9), 
                                    bg="white", fg="#666")
        self.instagram_label.pack(pady=2)
        
        self.twitter_label = Label(self.profile_frame, text="", font=("Arial", 9), 
                                  bg="white", fg="#666")
        self.twitter_label.pack(pady=2)
        
        # Copy Button
        copy_btn = Button(self.root, text="Copy Profile to Clipboard", 
                         command=self.copy_to_clipboard,
                         font=("Arial", 10), bg="#2196F3", fg="white",
                         padx=10, pady=3)
        copy_btn.pack(pady=10)
        
        # Footer
        footer = Label(self.root, text="Made with ❤️ and ☕", 
                      font=("Arial", 8), bg="#f0f0f0", fg="#999")
        footer.pack(pady=5)
        
        # Initialize with a profile
        self.generate_profile()
    
    def generate_profile(self):
        # Define data lists
        first_names = ["Alex", "Taylor", "Jordan", "Morgan", "Casey", "Riley", 
                      "Avery", "Quinn", "Jamie", "Cameron", "Skyler", "Emerson"]
        last_names = ["Johnson", "Smith", "Williams", "Brown", "Jones", "Garcia",
                     "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez"]
        usernames = ["cool_", "awesome_", "super_", "mega_", "ultra_", "pro_", 
                     "ninja_", "star_", "coolguy_", "tech_", "foodie_", "traveler_"]
        bios = [
            "Professional snack enthusiast. Delusional about avocado toast. Probably not a person.",
            "Mental health advocate and cat whisperer. My plants are more emotionally intelligent than most humans.",
            "Lifetime student of sarcasm. Celebrating my fifth year of being a morning person.",
            "Unapologetic coffee addict who thinks sleep is overrated. Can read through a book in one sitting.",
            "Banned from several beaches for being too photogenic. Everything is better with a little salt.",
            "Currently accepting applications for my personal sandwich. I'm very selective about my ingredients.",
            "Professional procrastinator. Genius level overthinker with a high tolerance for sarcasm.",
            "Selling my soul for better WiFi. Only kidding. Actually, looking for a good movie recommendation.",
            "Wannabe truth serum. Says things that aren't real but feel true. Professional conspiracy theorist.",
            "Ending world hunger with melt-in-your-mouth hot chocolate. Still working on the recipe.",
            "Caffeine dependent and drama free. Available for dance parties at 2am.",
            "Fancy man with keys for fingers. Currently practicing my signature dance move.",
            "Professional peanut butter aficionado with a complex relationship with my sandwich.",
            "Thinker so deep you need a life jacket. Cursed with unpredictable cleanliness.",
            "Recipe for happiness: lots of coffee, some sarcasm, and a whole lot of false confidence.",
            "Doyen of impossible dreams. Spectacular at not getting anything done.",
            "Renderer of injustice. Laptop, pint of ice cream, and a purple desk lamp in that exact order.",
            "Naysayer in a good way. Self-proclaimed expert on everything I've never actually done.",
            "Location unknown but rubbish is local. My bank account makes me feel like an industrial power plant.",
            "Saving the world one sandwich at a time. Also cosmos, pizza, and general philanthropy."
        ]
        traits = [
            "Has an allergy to disappointment",
            "Has a PhD in procrastination", 
            "Portfolio of 17 legally recognized stabbing techniques",
            "Definitely has a twitter account",
            "Skills include singing while sleeping",
            "Successfully completed 44 slumber parties",
            "Unofficially has 1040 correct answers to all life questions",
            "Skills include combining vague excitement with typical error 24/7",
            "Many opinions and no concerns about anything",
            "Started a revolution before it started",
            "Has an invisible tiny town called 'listless dessert'",
            "Combined persistence with unconventional bathroom habits",
            "Has a vintage all-purpose sword advantage in crisis situations",
            "Rate of regular humanity so-called 'sneaky' around the world",
            "Orbiter of his own game through the six thousand months [yet unknown]",
            "Capable of passionate eats with affection in many different ways",
            "Expert at sincerity and awkward silences",
            "Master of punchy manner and perfect mustaches"
        ]
        locations = [
            "Banana Republic", "Cloud City", "The Lazy Rev", "Mystic Coffee Shop", 
            "Under the Bridge", "The Office at 3 AM", "Moonymouth Bay", "Wannabe Miami",
            "Karma's Edge", "The Looming Beyond", "Summer Institute", "Harvest Mall",
            "Deep Space", "Botanical Gardens", "Wishful Thinking", "Coffee Pot"
        ]
        
        # Generate profile data
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        
        # Generate username
        username = random.choice(usernames) + ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        
        age = random.randint(18, 99)
        
        location = random.choice(locations)
        
        bio = random.choice(bios)
        
        # Generate traits (3 random traits)
        selected_traits = random.sample(traits, 3)
        traits_text = "Traits: " + ", ".join(selected_traits)
        
        instagram = f"@{username}"
        twitter = f"@{username}_cooler"
        
        # Update GUI elements
        self.name_label.config(text=name)
        self.username_label.config(text=f"@{username}")
        self.age_label.config(text=f"Age: {age}")
        self.location_label.config(text=f"Location: {location}")
        self.bio_label.config(text=f"Bio: {bio}")
        self.traits_label.config(text=traits_text)
        self.instagram_label.config(text=f"Instagram: {instagram}")
        self.twitter_label.config(text=f"Twitter: {twitter}")
        
        # Store the profile for copying
        self.current_profile = {
            "name": name,
            "username": username,
            "age": age,
            "location": location,
            "bio": bio,
            "traits": selected_traits,
            "instagram": instagram,
            "twitter": twitter
        }
    
    def copy_to_clipboard(self):
        profile_text = f"""Name: {self.current_profile['name']}
Username: @{self.current_profile['username']}
Age: {self.current_profile['age']}
Location: {self.current_profile['location']}
Bio: {self.current_profile['bio']}
Traits: {', '.join(self.current_profile['traits'])}
Instagram: {self.current_profile['instagram']}
Twitter: {self.current_profile['twitter']}
"""
        self.root.clipboard_clear()
        self.root.clipboard_append(profile_text)
        messagebox.showinfo("Copied", "Profile copied to clipboard!")

if __name__ == "__main__":
    root = Tk()
    app = FakeProfileGenerator(root)
    root.mainloop()