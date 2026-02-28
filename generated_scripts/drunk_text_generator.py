import random
import string
import re

class DrunkTextGenerator:
    def __init__(self):
        # Dictionary of words and their similar-sounding replacements
        self.similar_words = {
            'the': ['teh', 'th3', 'th'],
            'and': ['&', 'n', 'an'],
            'you': ['u', 'u', 'yuo'],
            'for': ['4', 'f', 'forr'],
            'with': ['w/', 'wit', 'wth'],
            'that': ['tht', 'tht', 'tht'],
            'have': ['hv', 'hae', 'hav'],
            'this': ['dis', 'tis', 'thi'],
            'they': ['thay', 'thye', 'thy'],
            'were': ['wer', 'wur', 'wre'],
            'been': ['b3n', 'be3n', 'ben'],
            'what': ['wht', 'wut', 'wht'],
            'from': ['frm', 'fr', 'fr0m'],
            'that': ['tht', 'tht', 'tht'],
            'there': ['thre', 'therr', 'thre'],
            'they': ['thay', 'thye', 'thy'],
            'would': ['wud', 'wud', 'wld'],
            'their': ['thier', 'thir', 'th3r'],
            'what': ['wht', 'wut', 'wht'],
            'your': ['ur', 'yr', 'yur'],
            'like': ['liek', 'lky', 'lik'],
            'just': ['jst', 'jus', 'jus'],
            'know': ['kno', 'knw', 'kno'],
            'people': ['peopl', 'ppl', 'peopel'],
            'could': ['cld', 'coul', 'coud'],
            'than': ['thn', 'thn', 'thn'],
            'then': ['thn', 'thn', 'thn'],
            'look': ['luk', 'lk', 'lkk'],
            'more': ['mre', 'mor', 'm0re'],
            'take': ['tke', 'tk', 'tak'],
            'time': ['tm', 'tme', 'timm'],
            'year': ['yr', 'yra', 'yee'],
            'into': ['nto', 'in2', 'int0'],
            'about': ['abt', 'abou', 'abt'],
            'know': ['kno', 'knw', 'kno'],
            'some': ['sum', 'sm', 'sme'],
            'them': ['thm', 'thm', 'thm'],
            'take': ['tke', 'tk', 'tak'],
            'them': ['thm', 'thm', 'thm'],
            'only': ['onli', 'onlyy', 'onl'],
            'other': ['ot', 'othr', 'ot'],
            'how': ['hw', 'h0w', 'hwa'],
            'word': ['wrd', 'wrd', 'w0rd'],
            'because': ['bcoz', 'bcuz', 'bc'],
            'going': ['goin', 'gng', 'goin'],
            'good': ['gd', 'gud', 'go0d'],
            'call': ['cal', 'calll', 'cals'],
            'make': ['mke', 'mk', 'mkae'],
            'here': ['hr', 'her', 'here'],
            'great': ['gr8', 'grt', 'gr8'],
            'really': ['rly', 'real', 'rly'],
            'people': ['ppl', 'peeps', 'peaple'],
            'say': ['sai', 'sayy', 'sae'],
            'things': ['thangs', 'thngs', 'thingz'],
            'back': ['bck', 'bk', 'backk'],
            'see': ['c', 's', 'se'],
            'now': ['nw', 'n0w', 'now'],
            'thought': ['thught', 'thot', 'thoht'],
            'use': ['us', 'u', 'us'],
            'work': ['wrk', 'w0rk', 'wor'],
            'first': ['1st', 'frst', 'fst'],
            'word': ['wrd', 'wr', 'w0rd'],
            'high': ['hgh', 'hgh', 'hig'],
            'life': ['lif', 'lif3', 'lfe'],
            'day': ['dy', 'dai', 'd1'],
            'get': ['gt', 'ge', 'get'],
            'give': ['giv', 'gve', 'giv'],
            'place': ['plac', 'plce', 'plae'],
            'found': ['fnd', 'foumd', 'f0und'],
            'turn': ['turn', 'tunr', 'trun'],
            'part': ['prt', 'pt', 'p0rt'],
            'case': ['cas', 'cae', 'case'],
            'most': ['mst', 'm0st', 'mst'],
            'find': ['fnd', 'findd', 'fined'],
            'end': ['nd', 'endd', 'end'],
            'group': ['grp', 'grup', 'group'],
            'hand': ['hnd', 'hnd', 'hend'],
            'old': ['ld', 'old', 'ol'],
            'line': ['ln', 'linee', 'ln'],
            'need': ['nd', 'n3ed', 'need'],
            'yes': ['yup', 'ys', 'ye'],
            'still': ['stll', 'stilll', 'stil'],
            'home': ['hom', 'hme', 'homee'],
            'thing': ['thg', 'thng', 'th1ng']
        }
        
        # Punctuation to add randomly
        self.punctuation = ['!', '?', '.', ',', ':', ';']
        
        # Characters that might cause capitalization errors
        self.common_caps_errors = {
            'i': 'I',
            'a': 'A',
            'o': 'O',
            'e': 'E',
            't': 'T'
        }
    
    def generate_drunk_text(self, text):
        """Generate drunk text from normal text"""
        # Split into words
        words = re.findall(r'\b\w+\b', text)
        
        # Process each word
        drunk_words = []
        for word in words:
            # Randomly decide whether to replace the word
            if random.random() < 0.3:  # 30% chance to replace
                if word.lower() in self.similar_words:
                    replacement = random.choice(self.similar_words[word.lower()])
                    # Capitalize first letter if original was capitalized
                    if word[0].isupper():
                        replacement = replacement.capitalize()
                    drunk_words.append(replacement)
                else:
                    # Randomly add a character or change case
                    if random.random() < 0.5:
                        # Add random punctuation at the end
                        extra_punct = random.choice(self.punctuation)
                        drunk_words.append(word + extra_punct)
                    else:
                        # Keep original but with potential capitalization error
                        drunk_words.append(self._add_caps_error(word))
            else:
                # Keep original word with possible capitalization error
                drunk_words.append(self._add_caps_error(word))
        
        # Join words back into sentence
        drunk_text = ' '.join(drunk_words)
        
        # Add random punctuation throughout
        drunk_text = self._add_random_punctuation(drunk_text)
        
        return drunk_text
    
    def _add_caps_error(self, word):
        """Add random capitalization errors"""
        if len(word) <= 1:
            return word
        
        # Randomly flip case of characters
        result = ""
        for char in word:
            if random.random() < 0.1 and char.isalpha():  # 10% chance to flip
                if char.islower():
                    result += char.upper()
                else:
                    result += char.lower()
            else:
                result += char
        
        # First letter randomization
        if random.random() < 0.2:  # 20% chance
            if result[0].islower():
                result = result[0].upper() + result[1:]
            else:
                result = result[0].lower() + result[1:]
        
        return result
    
    def _add_random_punctuation(self, text):
        """Add random punctuation throughout the text"""
        result = []
        for i, char in enumerate(text):
            result.append(char)
            # Add punctuation occasionally
            if char in string.ascii_letters and random.random() < 0.1:
                punct = random.choice(self.punctuation)
                # Don't add punctuation at the beginning or end
                if i > 0 and i < len(text) - 1:
                    result.append(punct)
        return ''.join(result)

import tkinter as tk
from tkinter import ttk, scrolledtext

class DrunkTextGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Drunk Text Generator")
        self.root.geometry("600x500")
        
        self.generator = DrunkTextGenerator()
        
        # Create widgets
        self.create_widgets()
        
        # Configure style
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat")
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Drunk Text Generator", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(input_frame, text="Enter your normal text:", 
                font=("Arial", 10)).pack(anchor=tk.W)
        
        self.input_text = scrolledtext.ScrolledText(input_frame, 
                                                    height=8, 
                                                    font=("Arial", 10))
        self.input_text.pack(fill=tk.X, pady=5)
        self.input_text.insert(tk.END, "The quick brown fox jumps over the lazy dog. This is a normal sentence that will be transformed into drunk text. It should look like it was written by someone who's had a few drinks.")
        
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.generate_button = tk.Button(button_frame, 
                                       text="Generate Drunk Text", 
                                       command=self.generate_text,
                                       font=("Arial", 12, "bold"),
                                       bg="#4CAF50",
                                       fg="white",
                                       padx=20,
                                       pady=5)
        self.generate_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(button_frame, 
                                    text="Clear", 
                                    command=self.clear_text,
                                    font=("Arial", 10),
                                    bg="#f44336",
                                    fg="white",
                                    padx=15,
                                    pady=5)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Output frame
        output_frame = tk.Frame(self.root)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(5, 20))
        
        tk.Label(output_frame, text="Drunk generated text:", 
                font=("Arial", 10)).pack(anchor=tk.W)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, 
                                                     height=8, 
                                                     font=("Arial", 10),
                                                     state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Footer
        footer = tk.Label(self.root, text="Randomly replaces words with similar-sounding ones, adds punctuation, and makes capitalization errors", 
                         font=("Arial", 8), 
                         fg="gray")
        footer.pack(pady=5)
    
    def generate_text(self):
        input_content = self.input_text.get("1.0", tk.END).strip()
        if not input_content:
            return
        
        drunk_text = self.generator.generate_drunk_text(input_content)
        
        # Update output text
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, drunk_text)
        self.output_text.config(state=tk.DISABLED)
    
    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = DrunkTextGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()