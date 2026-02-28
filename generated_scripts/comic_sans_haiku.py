import tkinter as tk
import os
import sys

# -------------------------------------------------
# Load recent search history
# -------------------------------------------------
HIST_FILE = "search_history.txt"
if os.path.exists(HIST_FILE):
    with open(HIST_FILE, "r", encoding="utf-8") as f:
        queries = [line.strip() for line in f if line.strip()]
else:
    # fallback sample data for demonstration
    queries = [
        "best python libraries 2025",
        "how to brew coffee",
        "vacation ideas near coast"
    ]

# Take up to three most recent queries
lines = queries[:3]
while len(lines) < 3:
    lines.append("")

# -------------------------------------------------
# Very simple 5‑7‑5 approximation
# -------------------------------------------------
def trim_to_approx(line, max_words):
    words = line.split()
    return " ".join(words[:max_words])

l1 = trim_to_approx(lines[0], 5)
l2 = trim_to_approx(lines[1], 7)
l3 = trim_to_approx(lines[2], 5)

haiku = f"{l1}\n{l2}\n{l3}"

# -------------------------------------------------
# Display haiku in Comic Sans (or nearest match)
# -------------------------------------------------
root = tk.Tk()
root.title("Personalized Haiku")

# Request Comic Sans; Tkinter will substitute if unavailable
font_style = ("Comic Sans MS", 28, "bold")

haiku_label = tk.Label(root, text=haiku, font=font_style, justify="center", wraplength=600, padx=20, pady=20)
haiku_label.pack()

root.mainloop()