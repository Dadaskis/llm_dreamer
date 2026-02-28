import tkinter as tk
import time
import re

class ClipboardMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.last_content = ""
        self.haiku_templates = {
            1: "One word you copied\nA haiku now in its place\nSimple and alone",
            2: "Two words were copied\nNow haiku replaces them\nCount is just two",
            3: "Three words you had\nHaiku springs into being\nThree is the count now",
            4: "Four words from you\nThis haiku takes their place now\nFour is the number",
            5: "Five words were pasted\nA haiku springs to life now\nCount of words is five",
            6: "Six words you shared\nNow haiku in their stead\nSix is the count",
            7: "Seven words you gave\nThis haiku replaces them\nSeven is the count",
            8: "Eight words you copied\nNow haiku in their place\nEight words counted",
            9: "Nine words were yours\nNow haiku takes their spot\nNine is the number",
            10: "Ten words you gave\nThis haiku replaces them\nTen words counted",
            "many": "Many words you copied\nThis haiku replaces them\nCount is in the lines"
        }
    
    def get_clipboard(self):
        try:
            return self.root.clipboard_get()
        except tk.TclError:
            return ""
    
    def set_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
    
    def count_words(self, text):
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        return len(words)
    
    def generate_haiku(self, count):
        if count in self.haiku_templates:
            return self.haiku_templates[count]
        return self.haiku_templates["many"]
    
    def monitor(self):
        current = self.get_clipboard()
        if current and current != self.last_content:
            word_count = self.count_words(current)
            if word_count > 0:
                haiku = self.generate_haiku(word_count)
                self.set_clipboard(haiku)
                self.last_content = haiku
            else:
                self.last_content = current
        self.root.after(500, self.monitor)
    
    def run(self):
        self.monitor()
        self.root.mainloop()

if __name__ == "__main__":
    monitor = ClipboardMonitor()
    monitor.run()