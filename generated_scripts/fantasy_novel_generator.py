import random
import textwrap

# Terrible name components
first_names = [
    "Zanril", "Krython", "Vexx", "Throkk", "Nyxxis", "Quorl", "Zylph", "Grolk",
    "Fyth", "Mordral", "Xyphos", "Kaelthas", "Voldoran", "Sythrax", "Drakol"
]
last_names = [
    "Shadowrend", "Skullcrusher", "Moonsunder", "Starborne", "Doomwhisper",
    "Winterfall", "Soulreap", "Firemaw", "Grimholt", "Dreadthorne"
]
titles = [
    "the Unwashed", "of the Shattered Spoon", "Who Forgets to Wear Pants",
    "the Mildly Inconvenienced", "with a Slight Hiccup", "the Utterly Average"
]

# Cliché plot elements
plot_points = [
    "discovers they are secretly the {title} of {place}",
    "is forced to flee their {humble_origin} after {random_event}",
    "finds a {magic_item} that may be {cliche_property}",
    "must unite the fractious {fantasy_race} clans",
    "learns the true meaning of friendship while fighting {monster}",
    "suffers a tragic loss when {unfortunate_event}",
    "receives cryptic prophecy from a {mysterious_figure}",
    "must choose between love and destiny",
    "discovers the villain is actually their {surprising_relation}",
    "wins the day through the power of {absurd_trope}"
]

# Setting components
places = [
    "Mistglut Peninsula", "The Soggy Steppes", "Mount Mundane", "Boringshire",
    "The Isle of Mild Discomfort", "Peril Plains (Mostly Just Grass)",
    "The Crapfellows", "Murswald"
]
humble_origins = [
    "turnip farm", "miserable village", "forgotten tavern", "sewage works",
    "mediocre bakery", "extremely boring mill"
]
magic_items = [
    "Spoon of Infinite Soup", "Boots of Slightly Faster Walking",
    "Helm of Mildly Improved Vision", "Amulet of Compromised Invincibility",
    "Scroll of Mostly Accurate Predictions"
]
cliche_properties = [
    "actually just a regular spoon", "cursed to cause slight indigestion",
    "more powerful than expected (but still weak)", "slightly haunted",
    "requiring regular polishing"
]
fantasy_races = [
    "mildly annoyed gnomes", "dwarves with poor posture", "elves with hay fever",
    "trolls with chronic back pain", "goblins with unfulfilled dreams"
]
monsters = [
    "Slightly Annoying Giant", "Disgruntled Badger", "Bored Dragon",
    "-angry goose swarm", "Grouchy Hill Giant with a Stubbed Toe"
]
unfortunate_events = [
    "a baking accident", "a misplaced comma in a contract", "mild spoilage",
    "a misunderstanding about footwear", "a dispute over tax law"
]
mysterious_figures = [
    "old man who won't stop talking about his cats", "mysterious hedge",
    "confused garden gnome", "person in a trench coat (clearly just a normal person)",
    "sentient puddle with attitude"
]
surprising_relations = [
    "long-lost cousin twice removed", "tax collector from 3 kingdoms over",
    "uncle who always wore that one weird hat", "neighbor who borrowed their hedge trimmer"
]
absurd_tropes = [
    "a well-timed sandwich", "interpretive dance", "off-key singing",
    "excessive paperwork", "a good old-fashioned sit-down talk"
]

# Chapter structures
chapter_templates = [
    "Of {unexpected_event}s and {mundane_item}s",
    "The {character} Who {unimpressive_action}",
    "In Which {character} Is Mildly Distressed",
    "{number} Ways to Almost Die (But Not Really)",
    "Tea, Tragedy, and Terrible Timing",
    "The {humble_object} of Destiny (Not That One)",
    "All Thisptical",
    "Meanwhile, In a Completely Different Part of the Forest..."
]

class FantasyNovelGenerator:
    def __init__(self):
        self.title = self.generate_title()
        self.characters = self.generate_characters()
        self.plot = self.generate_plot()
        self.chapters = self.generate_chapter_titles()
    
    def generate_title(self):
        prefixes = ["The", "A", "An", "The Absolute", "The Slightly"]
        suffixes = [
            "of Utter Mediocrity", "That Wasn't Even That Good",
            "That Everyone Forgot About", "with a Side of Regret",
            "in Three Parts (Mostly Filler)", "Mostly About Sandwiches"
        ]
        nouns = [
            "Prophecy", "Spoon", "Bureaucracy", "Reality Check",
            "Mild Inconvenience", "Disappointment", "Office Politics",
            "Meh"
        ]
        return f"{random.choice(prefixes)} {random.choice(nouns)} {random.choice(suffixes)}"
    
    def generate_character(self, role):
        first = random.choice(first_names)
        last = random.choice(last_names)
        title = random.choice(titles)
        full_name = f"{first} {last} {title}"
        return {
            "name": full_name,
            "role": role,
            "description": self.character_description(role)
        }
    
    def character_description(self, role):
        descriptions = {
            "protagonist": "An ordinary person with questionable life choices",
            "antagonist": "Actually not that bad, just misunderstood",
            "mentor": "Constantly losing train of thought",
            "sidekick": "Obsessed with a trivial hobby",
            "love_interest": "Has a surprisingly specific allergy",
            "comic_relief": "Only funny to themselves"
        }
        return descriptions.get(role, "Somewhat important")
    
    def generate_characters(self):
        character_roles = [
            "protagonist", "antagonist", "mentor", 
            "sidekick", "love_interest", "comic_relief"
        ]
        # Add 2-3 extra minor characters
        extra_roles = ["minor_villain", "helpful_stranger", "skeptical_villager"] * random.randint(2,3)
        all_roles = character_roles + extra_roles
        
        characters = []
        for role in all_roles:
            characters.append(self.generate_character(role))
        return characters
    
    def generate_plot(self):
        parts = []
        
        # Part 1: Setup
        protagonist = [c for c in self.characters if c["role"] == "protagonist"][0]
        place = random.choice(places)
        humble_origin = random.choice(humble_origins)
        
        parts.append(f"Introduction: {protagonist['name'].split(' ')[0]} lives in a {humble_origin} in {place}, dreaming of something vaguely better.")
        
        # Part 2: Inciting incident
        random_event = random.choice(["a poorly worded prophecy", "a misplaced tax document", "a baking contest gone wrong"])
        parts.append(f"Inciting Incident: {protagonist['name']} {random.choice(plot_points).format(place=place, humble_origin=humble_origin, random_event=random_event)}")
        
        # Part 3: Rising action
        for _ in range(random.randint(3,5)):
            parts.append(f"Development: {random.choice(self.characters)['name']} {random.choice(plot_points).format(place=random.choice(places), humble_origin=random.choice(humble_origins), random_event=random.choice(unfortunate_events))}")
        
        # Part 4: Climax
        antagonist = [c for c in self.characters if c["role"] == "antagonist"]
        if antagonist:
            parts.append(f"Climax: {protagonist['name']} confronts {antagonist[0]['name']} in {random.choice(places)}.")
            parts.append(f"Resolution: Through the power of {random.choice(absurd_tropes)}, {protagonist['name']} triumphs. Everyone learns a shallow lesson.")
        
        return parts
    
    def generate_chapter_titles(self):
        chapters = []
        for i in range(1, random.randint(15, 25)):
            template = random.choice(chapter_templates)
            formatted = template.format(
                unexpected_event=random.choice(unfortunate_events).lower(),
                mundane_item=random.choice(humble_origins).lower(),
                character=random.choice(self.characters)['name'].split(' ')[0],
                unimpressive_action=random.choice(["naps", "complains", "misplaces items", "forgets why they entered"]),
                humble_object=random.choice(magic_items).split(' of')[0].lower(),
                number=random.randint(2,12)
            )
            chapters.append(f"Chapter {i}: {formatted}")
        return chapters
    
    def __str__(self):
        output = []
        output.append("=" * 60)
        output.append(f"TITLE: {self.title}")
        output.append("=" * 60)
        output.append("\nMAIN CHARACTERS:")
        output.append("-" * 20)
        for char in self.characters[:6]:  # Show main characters
            output.append(f"{char['role'].upper()}: {char['name']}")
            output.append(f"   → {char['description']}")
        
        output.append("\n\nPLOT SUMMARY:")
        output.append("-" * 20)
        for i, point in enumerate(self.plot, 1):
            output.append(f"{i}. {point}")
        
        output.append("\n\nCHAPTER TITLES:")
        output.append("-" * 20)
        for chapter in self.chapters:
            output.append(chapter)
        
        output.append("\n" + "=" * 60)
        output.append("THE END? (Probably not, there's always a sequel)")
        output.append("=" * 60)
        
        return "\n".join(output)

def main():
    print("GENERATING TERRIBLE FANTASY NOVEL OUTLINE...\n")
    novel = FantasyNovelGenerator()
    print(novel)

if __name__ == "__main__":
    main()