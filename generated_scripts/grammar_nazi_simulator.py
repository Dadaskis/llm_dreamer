import tkinter as tk
from tkinter import scrolledtext
import re

class GrammarNaziSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Grammar Nazi Simulator")
        self.root.geometry("600x500")
        
        # Create widgets
        self.create_widgets()
        
        # Initialize text history
        self.history = []
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Grammar Nazi Simulator", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Instructions
        instructions = tk.Label(self.root, text="Type or paste text below. The Grammar Nazi will correct it with absurdly pedantic rules!", 
                               wraplength=550, justify="center")
        instructions.pack(pady=5)
        
        # Text input area
        self.input_text = scrolledtext.ScrolledText(self.root, height=10, width=70, font=("Arial", 10))
        self.input_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.input_text.insert(tk.END, "Type your text here...\n")
        
        # Correct button
        correct_button = tk.Button(self.root, text="Correct with Nazi Rules!", command=self.correct_text, 
                                 bg="red", fg="white", font=("Arial", 12, "bold"))
        correct_button.pack(pady=5)
        
        # Results area
        results_label = tk.Label(self.root, text="Nazi Corrections:", font=("Arial", 12, "bold"))
        results_label.pack(pady=5)
        
        self.results_text = scrolledtext.ScrolledText(self.root, height=10, width=70, font=("Arial", 10))
        self.results_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
    def correct_text(self):
        # Get input text
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert(tk.END, "Please enter some text to correct!")
            return
        
        # Apply absurd corrections
        corrected_text, corrections = self.apply_absurd_corrections(input_text)
        
        # Display results
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, corrected_text)
        
        # Add corrections list
        corrections_list = "\n".join([f"• {correction}" for correction in corrections])
        self.results_text.insert(tk.END, f"\n\nCorrections made:\n{corrections_list}")
        
        # Store in history
        self.history.append({
            'input': input_text,
            'output': corrected_text,
            'corrections': corrections
        })
    
    def apply_absurd_corrections(self, text):
        corrections = []
        result = text
        
        # --- Absurd Grammar Rules ---
        
        # Capitalize "the" in middle of sentences (absurd rule)
        def capitalize_the_match(match):
            return match.group(0).upper()
        
        # Find occurrences of "the" that are not at the beginning of sentences
        # (but allow at beginning of sentences or in middle with proper context)
        words = text.split()
        for i, word in enumerate(words):
            # Clean the word from punctuation
            clean_word = re.sub(r'[^\w]', '', word.lower())
            if clean_word == "the" and i != 0:
                # Add correction for capitalizing "the" in the middle
                corrections.append("You should capitalize 'the' in the middle of sentences (because we said so!)")
                
        # Capitalize every 3rd letter (absurd), but only sometimes
        if len(text) > 20 and sum(1 for c in text if c.isalpha()) > 20:
            result = ""
            letter_count = 0
            for char in text:
                if char.isalpha():
                    letter_count += 1
                    if letter_count % 3 == 0:
                        result += char.upper()
                    else:
                        result += char
                else:
                    result += char
            if letter_count > 0 and len(text) > 15:
                corrections.append("Capitalized every third letter - everywhere! (Grammar Nazi approved.)")
        
        # Add correction for double spaces
        if "  " in text:
            result = result.replace("  ", " ")
            corrections.append("Eliminated double spaces - we're not barbarians!")
        
        # Add correction for using "very" too often (unrealistic but pedantic)
        if text.lower().count("very") > 3:
            corrections.append("Reduced overuse of 'very' - enjoy your consistency!")
        
        # Insert "seriously" at beginning of sentences when not already present
        sentences = re.split(r'[.!?]+', text)
        for sentence in sentences:
            if sentence.strip() and not sentence.strip().startswith("Seriously"):
                break  # Only apply if we find a sentence without "Seriously"
        # This is just an example if we decide to apply it
        if len(text.split('.')) > 2 and len(text.split()) > 10:
            corrections.append("Added 'Seriously' to the beginning of sentences for emphasis (professional grading)")
        
        # Check for capitalization of pragmatic lexical items (absurd!)
        if "i" in text.lower() and "I" not in text and len(text.split()) > 1:
            corrections.append("You must capitalize 'i' when used as 'I' (meaningful for a computer program!)")
        
        # Make exclamation points more solemn (absurd rule)
        if text.count("!") > 0:
            # Just for fun - add a correction
            corrections.append("Exclamation points demoted to regular punctuation. Not everyone is so energetic.")
        
        # Make all commas "plentiful" by replacing with multiple commas
        if "," in text:
            corrections.append("Added extra commas for better separation (Czech grammar follicles in your writing!)")
            # This is more "house style" than a nonsense rule
        
        # Add correction about sentence structure (absurd) 
        if len(text.split('.')) > 2 and len(text) > 40:
            corrections.append("Sentences should be comma-split in third person for elegance.")
        
        # Add more absurd corrections - a few more examples that would make midnight laughter
        absurdist_elements = [
            "All terms should be replaced with vibratory sounds of exclamation!",
            "Italics are now banned for proper native honorifics!",
            "We require all caps pronunciation of proper nouns! (Mistakenly called blossom words.)",
            "Un-transformed exclamation-points are tolerated only with consensus!",
        ]
        
        # Add one randomly chosen absurd rule (so it's consistent with nature of the program)
        import random
        if random.random() > 0.5:
            corrections.append(random.choice(absurdist_elements))
        
        # Final correction - gentle reminder about grammatical again
        corrections.append("Your sentence liberties are acceptable to the Grammar Nazi. Pedantry complete.")
        
        # Return corrected text and list of absurd corrections
        return result, corrections[:5]  # Limit to 5 corrections to prevent overwhelming

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarNaziSimulator(root)
    root.mainloop()