import tkinter as tk
import random
import threading
import time

class PigeonSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Pigeon Simulator")
        self.root.geometry("400x300")
        
        self.messages = [
            "I am a pigeon",
            "Pigeon power!",
            "Coo coo!",
            "Birdie mode activated",
            "Feathered friend here",
            "Pigeon vibes only",
            "Tweet tweet!",
            "Urban avian",
            "Pigeon life",
            "Bird brain alert"
        ]
        
        self.is_running = False
        self.message_label = tk.Label(root, text="", font=("Arial", 16), wraplength=350)
        self.message_label.pack(expand=True)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        
        self.start_button = tk.Button(self.button_frame, text="Start Pigeons", command=self.start_pigeons)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(self.button_frame, text="Stop Pigeons", command=self.stop_pigeons)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(self.button_frame, text="Clear Messages", command=self.clear_messages)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.pigeon_thread = None
        
    def start_pigeons(self):
        if not self.is_running:
            self.is_running = True
            self.pigeon_thread = threading.Thread(target=self.pigeon_worker, daemon=True)
            self.pigeon_thread.start()
            
    def stop_pigeons(self):
        self.is_running = False
        
    def clear_messages(self):
        self.message_label.config(text="")
        
    def pigeon_worker(self):
        while self.is_running:
            message = random.choice(self.messages)
            self.root.after(0, self.update_message, message)
            sleep_time = random.uniform(1, 5)
            time.sleep(sleep_time)
            
    def update_message(self, message):
        self.message_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PigeonSimulator(root)
    root.mainloop()