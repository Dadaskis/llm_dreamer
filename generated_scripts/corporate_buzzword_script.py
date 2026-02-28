import random
import textwrap

# Corporate buzzword components
BUZZWORDS = [
    "synergy", "disrupt", "paradigm", "leverage", "optimize",
    "streamline", "holistic", "scalable", "agile", "customer-centric",
    "data-driven", "innovative", "next-gen", "cutting-edge", "best-of-breed",
    "mission-critical", "value-add", "blue-sky", "low-hanging fruit", "bandwidth"
]

NOUNS = [
    "solution", "platform", "framework", "ecosystem", "pipeline",
    "paradigm", "workflow", "infrastructure", "architecture", "methodology",
    "ROI", "KPI", "dashboard", "analytics", "big data",
    "cloud", "AI", "blockchain", "IoT", "digital transformation",
    "blockchain", "synergy", "bandwidth", "scalability", "deliverable"
]

VERBS = [
    "leverage", "optimize", "streamline", "disrupt", "innovate",
    "integrate", "iterate", "monetize", "personalize", "scale",
    "transform", "revolutionize", "enhance", "drive", "empower",
    "orchestrate", "reimagine", "redefine", "pivot", "embark"
]

TEMPLATES = [
    "{} the {} to unlock {} value",
    "{} {} through {} initiatives",
    "{} {}: a {} approach",
    "{} {} with {} solutions",
    "{} {} via {} frameworks",
    "{} {} for {} outcomes",
    "{} {} using {} strategies",
    "{} {} in a {} manner",
    "{} {} by {} methodologies",
    "{} {} towards {} transformation"
]

def generate_buzz_phrase(complexity=1):
    """Generate an increasingly absurd buzzword phrase"""
    template = random.choice(TEMPLATES)
    
    # Increase complexity by adding more buzzwords
    if complexity > 1:
        parts = template.split()
        # Insert extra buzzwords at random positions
        for _ in range(min(complexity-1, 3)):
            insert_pos = random.randint(1, len(parts)-1)
            parts.insert(insert_pos, random.choice(BUZZWORDS))
        template = " ".join(parts)
    
    # Fill template with random words
    placeholders = template.count("{}")
    words = []
    for _ in range(placeholders):
        word_type = random.choice(["buzz", "noun", "verb"])
        if word_type == "buzz":
            words.append(random.choice(BUZZWORDS))
        elif word_type == "noun":
            words.append(random.choice(NOUNS))
        else:
            words.append(random.choice(VERBS))
    
    try:
        return template.format(*words)
    except:
        # Fallback if formatting fails
        return f"{random.choice(VERBS)} {random.choice(NOUNS)} with {random.choice(BUZZWORDS)}"

def generate_slide_title(absurdity_level):
    """Generate increasingly absurd slide titles"""
    patterns = [
        f"{random.choice(BUZZWORDS).title()} {random.choice(NOUNS).title()}",
        f"{random.choice(BUZZWORDS).title()}ing {random.choice(NOUNS)}",
        f"The {random.choice(BUZZWORDS)} of {random.choice(NOUNS)}",
        f"{random.choice(BUZZWORDS).title()}-Driven {random.choice(NOUNS).title()}",
        f"{random.choice(BUZZWORDS).title()} {random.choice(NOUNS)}: A {random.choice(BUZZWORDS)} Perspective"
    ]
    
    # Add extra buzzwords for higher absurdity
    if absurdity_level > 2:
        extra = " ".join([random.choice(BUZZWORDS) for _ in range(absurdity_level-2)])
        return f"{extra} {patterns[absurdity_level % len(patterns)]}"
    
    return patterns[absurdity_level % len(patterns)]

def generate_presentation(num_slides=8):
    """Generate a complete absurd corporate presentation"""
    slides = []
    
    for i in range(num_slides):
        absurdity = min(i + 1, 5)  # Increase absurdity with each slide
        
        # Generate title
        title = generate_slide_title(absurdity)
        
        # Generate bullet points
        bullets = []
        for _ in range(random.randint(3, 5)):
            phrase = generate_buzz_phrase(absurdity)
            # Add corporate padding
            padding_options = [
                f"to drive business value",
                f"in the digital age",
                f"for maximum impact",
                f"across the enterprise",
                f"in a post-pandemic world"
            ]
            if random.random() > 0.6:
                phrase += f" {random.choice(padding_options)}"
            bullets.append(f"• {phrase}")
        
        slides.append({
            'title': title,
            'bullets': bullets
        })
    
    return slides

def print_presentation(slides):
    """Print the presentation formatted"""
    print("=" * 60)
    print("ABSURD CORPORATE BUZZWORD PRESENTATION")
    print("=" * 60)
    print()
    
    for i, slide in enumerate(slides, 1):
        print(f"SLIDE {i}: {slide['title']}")
        print("-" * 40)
        for bullet in slide['bullets']:
            print(textwrap.fill(bullet, width=56, subsequent_indent='  '))
        print()

def main():
    """Main function with some variety"""
    print("\nGenerating increasingly absurd corporate presentation...\n")
    
    # Generate with some randomness in slide count
    slides = generate_presentation(random.randint(5, 10))
    print_presentation(slides)
    
    # Print a "key takeaway" at the end
    takeaways = [
        "Key Takeaway: Synergize verticals to disrupt the paradigm.",
        "Key Takeaway: Leverage scalable solutions for optimal ROI.",
        "Key Takeaway: Empower teams to innovate with bleeding-edge tech.",
        "Key Takeaway: Orchestrate digital transformation across ecosystems."
    ]
    print("=" * 60)
    print(random.choice(takeaways))
    print("=" * 60)
    print()

if __name__ == "__main__":
    main()