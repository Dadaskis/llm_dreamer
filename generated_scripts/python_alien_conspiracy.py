import praw
import random
import datetime
import textwrap

# ==== CONFIGURATION ====
REDDIT_CLIENT_ID = "YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDDIT_USER_AGENT = "PythonAlienConspiracyBot by /u/yourusername"
SUBREDDIT_NAME = "YourSubredditHere"  # e.g., "conspiracy", "python"

# Sample sections of the conspiracy
SECTIONS = [
    "Python's design was dictated by an ancient alien race that seeded Earth with advanced mathematics.",
    "The serpent logo is a direct homage to the Draco constellation, where the original 'serpent' was an alien emissary.",
    "Guido van Rossum allegedly received his inspiration during a close encounter with unidentified lights in the Dutch sky.",
    "The language's garbage collector mimics the way alien bio‑machines recycle organic waste.",
    "Python's dynamic typing mirrors the fluid reality‑distortion fields used by extraterrestrials.",
    "The extensive standard library is a coded map of interstellar star systems."
]

HOOKS = [
    "Did you know?",
    "Fact:",
    "Here's the truth:",
    "Consider this:",
    "Remember when:",
    "You might think:",
]

ENDING_HASHTAGS = [
    "#PythonAlienConspiracy #CodeFromStars",
    "#AlienProgrammers #PythonIsNotFromHere",
    "#ExtraterrestrialsLovePython #CodeConquest",
    "#HiddenMessageInPython #CosmicSyntax"
]

# ==== REDDIT INITIALIZATION ====
r = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)

# ==== CONSTRUCT POST ====
today = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
chosen_hook = random.choice(HOOKS)
chosen_section = random.choice(SECTIONS)
chosen_endings = random.sample(ENDING_HASHTAGS, k=2)

post_title = f"{chosen_hook} Why Python Is Secretly an Alien Language"
selftext = f"""{chosen_section}

🕒 Posted on {today}

{chosen_section}

🔎 **Additional clues**:
- Guido's surname "van Rossum" loosely translates to "from the Rossum island", an anagram of "Roswell"? 
- Python 2.7 was released in 2000, the same year as the alleged "Roswell Incident 2.0".
- The `async` and `await` syntax began appearing just as more people reported UFO sightings.

*Disclaimer*: This is a purely fictional narrative crafted for entertainment. No actual evidence supports an extraterrestrial origin for Python.

{chosen_endings[0]} {chosen_endings[1]}
"""

# ==== SUBMIT TO REDDIT ====
subreddit = r.subreddit(SUBREDDIT_NAME)

submission = subreddit.submit(
    title=post_title,
    selftext=selftext,
    flair_id=None  # adjust if your subreddit uses specific flairs
)

print(f"Submitted post: {submission.title}")  # Simple confirmation output