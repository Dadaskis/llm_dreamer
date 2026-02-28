import tkinter as tk
from tkinter import ttk
import random

class ClassroomGradeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Classroom Grade Calculator")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        
        # Define some funny reasons for grades
        self.reasons = [
            "B- because you looked at the ceiling too much",
            "B+ because you asked a question at the perfect time",
            "A- because you actually showed up to class",
            "C+ because you were close to an A on the test",
            "B because you didn't talk to the professor after class",
            "D+ because you came to class on time but only stayed for 5 minutes",
            "B+ because you had the right answer when the teacher asked for volunteers",
            "C- because you helped another student",
            "A because you were the first to raise your hand to answer questions",
            "B- because you slept through 3 of the 4 classes",
            "C because you understood almost everything but forgot to write the name",
            "B+ because you made the teacher laugh during a difficult lesson",
            "D- because the teacher noticed you were napping but let it slide",
            "A- because you brought a snack for the class",
            "B because you used a really fancy pen for your notes",
            "C+ because you had the right answer but the teacher had a hard time writing",
            "B+ because you had the perfect amount of shoulder-length hair",
            "D because you gave the wrong excuse for not doing homework",
            "A+ because you aced 3 out of 4 questions",
            "B- because you sat in the back row and complained about the sound quality"
        ]
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Classroom Grade Calculator", 
                              font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=20)
        
        # Student name input
        name_frame = tk.Frame(self.root, bg="#f0f0f0")
        name_frame.pack(pady=10)
        
        tk.Label(name_frame, text="Student Name:", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT)
        self.name_entry = tk.Entry(name_frame, font=("Arial", 12), width=20)
        self.name_entry.pack(side=tk.LEFT, padx=10)
        
        # Grade input
        grade_frame = tk.Frame(self.root, bg="#f0f0f0")
        grade_frame.pack(pady=10)
        
        tk.Label(grade_frame, text="Current Grade (0-100):", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT)
        self.grade_entry = tk.Entry(grade_frame, font=("Arial", 12), width=10)
        self.grade_entry.pack(side=tk.LEFT, padx=10)
        
        # Calculate button
        self.calculate_button = tk.Button(self.root, text="Calculate Final Grade", 
                                         font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                                         command=self.calculate_grade)
        self.calculate_button.pack(pady=20)
        
        # Result frame
        result_frame = tk.Frame(self.root, bg="#f0f0f0")
        result_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        tk.Label(result_frame, text="Result:", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
        
        self.result_text = tk.Text(result_frame, font=("Arial", 12), height=10, width=50, wrap=tk.WORD)
        self.result_text.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Scrollbar for result text
        scrollbar = tk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        
        # Clear button
        clear_button = tk.Button(self.root, text="Clear Results", 
                                font=("Arial", 10), bg="#f44336", fg="white",
                                command=self.clear_results)
        clear_button.pack(pady=10)
        
    def calculate_grade(self):
        # Get inputs
        name = self.name_entry.get().strip()
        grade_input = self.grade_entry.get().strip()
        
        # Validate inputs
        if not name:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter a student name.")
            return
            
        try:
            grade = float(grade_input)
            if grade < 0 or grade > 100:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "Please enter a grade between 0 and 100.")
                return
        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter a valid number for the grade.")
            return
        
        # Calculate final grade with random factors
        final_grade = grade
        
        # Apply random adjustments (up to 10 points either way)
        adjustment = random.randint(-10, 10)
        final_grade += adjustment
        
        # Clamp to valid range
        final_grade = max(0, min(100, final_grade))
        
        # Get random reason
        reason = random.choice(self.reasons)
        
        # Determine letter grade
        if final_grade >= 90:
            letter_grade = "A"
        elif final_grade >= 80:
            letter_grade = "B"
        elif final_grade >= 70:
            letter_grade = "C"
        elif final_grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
            
        # Display result
        self.result_text.delete(1.0, tk.END)
        result = f"Student: {name}\n"
        result += f"Original Grade: {grade:.1f}\n"
        result += f"Adjustment: {adjustment:+.1f}\n"
        result += f"Final Grade: {final_grade:.1f} ({letter_grade})\n\n"
        result += f"Reason: {reason}"
        
        self.result_text.insert(tk.END, result)
        
    def clear_results(self):
        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClassroomGradeCalculator(root)
    root.mainloop()