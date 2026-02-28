import tkinter as tk
from tkinter import ttk
import random

class FakeDoctorNoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Doctor's Note Generator")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f8ff")
        
        # Fake medical terms
        self.diagnoses = [
            "Chronic Peculiar Sensation Disorder",
            "Temporary Unexplained Brightness Syndrome",
            "Intermittent Light Sensitivity Syndrome",
            "Involuntary Musical Note Syndrome",
            "Unexplained Fidgeting Disorder",
            "Occasional Head Nodding Syndrome",
            "Sudden Channel Changing Tendency",
            "Unusual Hair Growth Pattern Disorder",
            "Periodic Epileptic Muttering",
            "Random Internet Research Disorder",
            "Unexplained Bent Back Syndrome",
            "Mysterious Prone to Sneeze Condition",
            "Unusual Pencil Grip Syndrome",
            "Intermittent Inability to Be Serious",
            "Occasional Euphoric Laughter Disorder"
        ]
        
        self.treatments = [
            "Prescribe 3-4 hours of daily meditation",
            "Recommend 2 cups of coffee before 2 PM",
            "Suggest taking 30-minute naps",
            "Order 17 mock medical consultations",
            "Prescribe 24/7 sleeping hammock",
            "Recommend daily stretching exercises",
            "Suggest taking 10 deep breaths hourly",
            "Prescribe 47 hours of nighttime sleep",
            "Recommend switching to tablet instead of phone",
            "Order 14 days of 'nothing much' therapy",
            "Suggest reading comic books for 15 minutes",
            "Prescribe 5 Selfie-a-Day sessions",
            "Recommend 27 minutes of 'resting the eyes'",
            "Order comprehensive coffee addiction removal plan",
            "Suggest delegation of all work to AI"
        ]
        
        self.advice = [
            "Relax and enjoy the chaos around you.",
            "Remember to be patient with the strange symptoms.",
            "Eat at least 5 full meals per day.",
            "Stay hydrated and more importantly, stay caffeinated.",
            "Keep a positive outlook while in the 'unknown zone'.",
            "Do not consult your own thoughts for medical opinions.",
            "Maintain regular contact with friends and family.",
            "Re-evaluate priorities frequently because they change.",
            "Avoid attempting to fix everything yourself.",
            "Believe in the magic of surprise and occurances.",
            "Sleep is an optional activity for flyers.",
            "Pamper yourself in the name of calming.",
            "Speak to your medical team daily - even if it's just to complain.",
            "Take this as a worthy journey of integration.",
            "Frequency of strange hiccups is desired."
        ]
        
        # Header
        header_frame = tk.Frame(root, bg="#4682b4", pady=15)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="🎲 Fake Doctor's Note Generator 🩺", 
                              font=("Arial", 20, "bold"), bg="#4682b4", fg="white")
        title_label.pack()
        
        # Main content
        content_frame = tk.Frame(root, bg="#f0f8ff", padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Instructions
        instructions = tk.Label(content_frame, text="Click 'Generate Random Note' to create a hilarious fake doctor's note!",
                               font=("Arial", 12), bg="#f0f8ff", fg="#333333", justify=tk.CENTER)
        instructions.pack(pady=(0, 20))
        
        # Note frame
        note_frame = tk.Frame(content_frame, bg="white", relief=tk.RAISED, bd=2)
        note_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.note_text = tk.Text(note_frame, wrap=tk.WORD, width=60, height=15, 
                                font=("Arial", 11), bg="#fff8dc", fg="#2c3e50")
        self.note_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(note_frame, command=self.note_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.note_text.config(yscrollcommand=scrollbar.set)
        
        # Buttons
        button_frame = tk.Frame(content_frame, bg="#f0f8ff")
        button_frame.pack(pady=10)
        
        generate_btn = tk.Button(button_frame, text="Generate Random Note", 
                               command=self.generate_note,
                               font=("Arial", 12, "bold"), bg="#32cd32", fg="white",
                               padx=20, pady=10, relief=tk.RAISED, bd=2)
        generate_btn.pack(side=tk.LEFT, padx=10)
        
        clear_btn = tk.Button(button_frame, text="Clear Note", 
                            command=self.clear_note,
                            font=("Arial", 12), bg="#ff6347", fg="white",
                            padx=20, pady=10, relief=tk.RAISED, bd=2)
        clear_btn.pack(side=tk.LEFT, padx=10)
        
        # Footer
        footer_frame = tk.Frame(root, bg="#4682b4", pady=10)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_label = tk.Label(footer_frame, text="This is a parody generator for comedic purposes only",
                               font=("Arial", 9), bg="#4682b4", fg="white")
        footer_label.pack()
        
        # Generate initial note
        self.generate_note()
    
    def generate_note(self):
        # Get random elements
        diagnosis = random.choice(self.diagnoses)
        treatment = random.choice(self.treatments)
        advice = random.choice(self.advice)
        
        # Create a fake medical note
        note = f"""
                               DOCTOR'S NOTE

PATIENT: Random Individual
DATE: {random_date()}
DIAGNOSIS: {diagnosis}

CLINICAL OBSERVATIONS:
The patient exhibits notable {advice.lower()} 

TREATMENT RECOMMENDATIONS:
{treatment}. 
This treatment requires {random_int(2,5)} consecutive days of compliance.

ADDITIONAL NOTES:
Patient should maintain {random_int(3,8)} hour sleep cycle.
Avoid use of {random_object()} for 3 days.
Report any visible manifestation of {random_color()} over time.

MEDICAL STAFF:
Dr. {random_name()} ({random_int(1000, 9999)})
"""

        # Display the note
        self.note_text.delete(1.0, tk.END)
        self.note_text.insert(tk.END, note)
        
        # Add some styling
        self.note_text.tag_configure("header", font=("Arial", 14, "bold"), foreground="#2c3e50")
        self.note_text.tag_configure("diagnosis", font=("Arial", 12, "italic"), foreground="#c0392b")
        self.note_text.tag_configure("treatment", font=("Arial", 11), foreground="#27ae60")
        self.note_text.tag_configure("footer", font=("Arial", 9), foreground="#7f8c8d")
        
        self.note_text.tag_add("header", "1.0", "1.30")
        self.note_text.tag_add("diagnosis", "7.0", "7.30")
        self.note_text.tag_add("treatment", "11.0", "12.30")

    def clear_note(self):
        self.note_text.delete(1.0, tk.END)

def random_date():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    day = random.randint(1, 30)
    month = random.choice(months)
    year = random.randint(2019, 2024)
    return f"{month} {day}, {year}"

def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def random_object():
    objects = ["donut", "sock", "plant", "box", "remote", "paper", "pen", "cup", "book", "phone"]
    return random.choice(objects)

def random_color():
    colors = ["purple", "orange", "green", "red", "blue", "yellow", "pink", "brown"]
    return random.choice(colors)

def random_name():
    first_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    last_names = ["PhD", "Jr.", "Sr.", "II", "III", "IV", "V"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeDoctorNoteGenerator(root)
    root.mainloop()