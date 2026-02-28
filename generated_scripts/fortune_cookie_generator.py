import random

def make_fortune_cookie():
    # Define lists of random elements for reviews
    adjectives = ["amazing", "terrible", "incredible", "disappointing", "wonderful", "bizarre", "delicious", "horrible", "fantastic", "awful", "surprising", "forgettable", "memorable", "odd", "ordinary", "exceptional", "mediocre", "unforgettable", "strange", "delightful"]
    places = ["restaurant", "café", "bistro", "diner", "establishment", "joint", "eatery", "place", "hole", "spot", "tavern", "cuisine", "delight", "haven", "oasis", "hideaway", "rendezvous", "refuge", "sanctuary", "paradise"]
    verbs = ["left me speechless", "floored me", "broke my heart", "made my day", "deteriorated my mood", "gave me hope", "shattered my expectations", "renewed my faith", "boggled my mind", "crushed my dreams", "enchanted me", "confused me", "amazed me", "excited me", "depressed me", "inspired me", "annoyed me", "thrilled me", "disgusted me", "delighted me"]
    objects = ["food", "service", "experience", "menu", "waiter", "waitress", "owner", "staff", "ambiance", "decor", "music", "table", "utensils", "sauce", "drink", "dessert", "appetizer", "entree", "side dish", "bill", "cleanliness"]
    intensifiers = ["completely", "utterly", "absolutely", "incredibly", "totally", "extremely", "remarkably", "exceptionally", "astonishingly", "mind-bogglingly", "unbelievably", "incredulously", "surprisingly", "unexpectedly", "curiously", "strangely"]
    actions = ["recommended it to everyone", "walked out in disgust", "came back three times", "ordered the same dish twice", "charmed by the staff", "stood there in shock", "ordered the same item seven times", "ignored the terrible service", "had an epiphany", "screamed in delight", "gave up hope of ever eating here again", "realized I hate this place", "couldn't stop talking about it", "questioned all my life choices"]
    outcomes = ["since then I've never been back", "but I'll keep coming", "and I've never been happier", "so I started a social media campaign", "and now I live here for a month", "but the value was worth it", "and I'll never try anything else", "but the experience was unforgettable", "so I've become obsessed", "but it got worse", "and now I'm here to review your food", "but I got a good deal", "and it completely changed my life", "but I'm a regular now", "and I've sworn off restaurants forever", "so I started my own business"]
    
    # Generate random review components
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    place = random.choice(places)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    intensifier = random.choice(intensifiers)
    action = random.choice(actions)
    outcome = random.choice(outcomes)
    
    # Create different review formats
    review_formats = [
        f"This {place} is {adj1}! The {obj} was {intensifier} {adj2}, and it really {verb}. I {action} {outcome}.",
        f"I visited this {place} and {verb}! The {obj} was {intensifier} {adj2} - I {action} {outcome}.",
        f"Never in my life have I seen {adj1} {obj} at a {place}! It {verb} - I {action} {outcome}.",
        f"Spent my lunch at this {place} - {intensifier} {adj1} experience with {adj2} {obj}. It {verb}, I {action} {outcome}.",
        f"This {place} was {adj1}! The {obj} was {intensifier} {adj2} and {verb}. I {action} and {outcome}."
    ]
    
    return random.choice(review_formats)

# Generate a fortune cookie
print("\n" + "="*50)
print("YOUR FORTUNE COOKIE")
print("="*50)
print(make_fortune_cookie())
print("="*50)
print("\nENJOY YOUR MEAL!")