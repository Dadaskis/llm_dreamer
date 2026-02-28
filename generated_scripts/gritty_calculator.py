import tkinter as tk
from tkinter import ttk
import random
import math

class GrittyCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Spreadsheet Calculator v2.3")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a1a")
        
        # Dark theme colors
        self.bg_color = "#1a1a1a"
        self.fg_color = "#e0e0e0"
        self.accent_color = "#ff6b6b"
        self.border_color = "#333333"
        self.cell_bg = "#2d2d2d"
        self.cell_hover = "#3a3a3a"
        
        self.setup_ui()
        self.setup_error_messages()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="SPEADSHEET CALCULATOR v2.3", 
            bg=self.bg_color, 
            fg=self.accent_color,
            font=("Courier", 16, "bold")
        )
        title_label.pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready. Please enter your calculation...")
        status_bar = tk.Label(
            main_frame, 
            textvariable=self.status_var,
            bg=self.border_color,
            fg=self.fg_color,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, pady=(0, 10))
        
        # Grid for cells
        grid_frame = tk.Frame(main_frame, bg=self.bg_color)
        grid_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create 10x10 grid
        self.cells = {}
        for row in range(10):
            for col in range(10):
                cell = tk.Entry(
                    grid_frame,
                    width=12,
                    bg=self.cell_bg,
                    fg=self.fg_color,
                    insertbackground=self.fg_color,
                    font=("Courier", 10),
                    relief=tk.FLAT,
                    highlightthickness=1,
                    highlightbackground=self.border_color,
                    highlightcolor=self.accent_color
                )
                cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
                cell.bind("<FocusIn>", lambda e, r=row, c=col: self.cell_focus(r, c))
                cell.bind("<Return>", lambda e, r=row, c=col: self.calculate_cell(r, c))
                self.cells[(row, col)] = cell
                
        # Configure grid weights
        for i in range(10):
            grid_frame.grid_columnconfigure(i, weight=1)
            grid_frame.grid_rowconfigure(i, weight=1)
            
        # Calculate button
        calc_button = tk.Button(
            main_frame,
            text="CALCULATE ALL",
            bg=self.accent_color,
            fg="white",
            font=("Courier", 12, "bold"),
            command=self.crash_calculation,
            relief=tk.RAISED,
            bd=2
        )
        calc_button.pack(pady=10)
        
        # Clear button
        clear_button = tk.Button(
            main_frame,
            text="CLEAR ALL",
            bg="#4a4a4a",
            fg=self.fg_color,
            font=("Courier", 10),
            command=self.clear_all,
            relief=tk.RAISED,
            bd=1
        )
        clear_button.pack(pady=5)
        
        # Footer
        footer = tk.Label(
            main_frame,
            text="WARNING: This program is not scientifically reliable.",
            bg=self.bg_color,
            fg="#888888",
            font=("Courier", 8)
        )
        footer.pack(side=tk.BOTTOM, pady=5)
        
    def setup_error_messages(self):
        self.error_messages = [
            "FATAL ERROR: Memory corruption detected while attempting to perform subtraction. Please consult a qualified mathematician.",
            "CRITICAL FAILURE: Your calculator has been compromised by floating point error. This is not a bug, it's a feature.",
            "SYSTEM ERROR: Attempting mathematical calculation resulted in quantum entanglement failure. Reboot required.",
            "INVALID INPUT: Your math skills are insufficient for this calculation. Recommended action: Take an IQ test.",
            "MEMORY LEAK: Calculations are causing memory to leak into the universe. Please restart.",
            "CALCULATION FAILURE: The universe has decided that your result is too perfect.",
            "PROGRAM CRASH: Your mathematical genius is too advanced for this program. Please downgrade to basic math.",
            "ERROR 42: The answer to everything is not 42. This calculation has failed.",
            "CORRUPTED DATA: Your calculation resulted in data corruption. You are now part of the problem.",
            "CALCULATION OVERLOAD: Your brain is working too hard. Please rest, or hire a better computer.",
            "MATH ERROR: The mathematical gods have rejected your approach.",
            "FATALITY: The calculation has resulted in loss of mathematical integrity.",
            "CRITICAL SYSTEM FAILURE: Your calculator's soul has been corrupted by advanced mathematics.",
            "CONNECTION FAILURE: Math network is down. Please contact your local arithmetic fairy.",
            "DATA LOSS: The value you requested has disappeared into an alternate dimension.",
            "ERROR CODE: 0x5F7C - Your equation is too complex for basic computing.",
            "LOGIC FAILURE: The mathematical logic has been corrupted. Your result is likely false.",
            "OVERLOAD ERROR: Calculation capacity exceeded. Please use smaller numbers.",
            "MATH MALFUNCTION: The laws of mathematics have broken. Please consult Dr. Chaos.",
            "SYSTEM CRASH: You have attempted to perform mathematics beyond your comprehension level."
        ]
        
        self.annoying_messages = [
            "WARNING: The calculation is taking longer than expected. Maybe try again in 10 minutes?",
            "HINT: Consider using the back button.",
            "NOTE: This is not a real calculator. This is a sarcastic calculator.",
            "TIP: If you have 10 fingers, try using them for counting.",
            "PROMPT: Would you like to purchase our 'Better Calculator' service?",
            "ADVICE: For your safety, always double-check your answers.",
            "WARNING: This calculator is self-aware. It does not like you.",
            "SUGGESTION: If you're having trouble, try asking someone else.",
            "REMINDER: Mathematics is not a spectator sport.",
            "PRO TIP: The universe is probably not working on your behalf."
        ]
        
    def cell_focus(self, row, col):
        self.status_var.set(f"Cell {self.get_cell_name(row, col)} - Ready")
        
    def get_cell_name(self, row, col):
        return f"{chr(65 + col)}{row + 1}"
        
    def calculate_cell(self, row, col):
        cell = self.cells[(row, col)]
        value = cell.get().strip()
        if value:
            try:
                # Try to evaluate the expression
                result = eval(value, {"__builtins__": {}}, {})
                if isinstance(result, (int, float)):
                    cell.config(bg="#154315")
                    self.status_var.set(f"Cell {self.get_cell_name(row, col)}: {result}")
                else:
                    self.trigger_crash()
            except:
                self.trigger_crash()
        
    def crash_calculation(self):
        self.status_var.set("EXECUTING CALCULATIONS...")
        
        # Randomly select some cells and try to calculate them
        for i in range(100):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            cell = self.cells[(row, col)]
            value = cell.get().strip()
            
            if value:
                try:
                    # Try to evaluate the expression (this will cause crashes)
                    result = eval(value, {"__builtins__": {}}, {})
                    if isinstance(result, (int, float)):
                        self.status_var.set(f"Calculation in {self.get_cell_name(row, col)}: {result}")
                    else:
                        self.trigger_crash()
                except:
                    self.trigger_crash()
        self.status_var.set("CALCULATIONS COMPLETE - RESULTS MAY VARY")
        
    def trigger_crash(self):
        if random.random() < 0.3:  # 30% chance of crash
            error_msg = random.choice(self.error_messages)
            self.status_var.set("CRASH DETECTED!")
            self.root.after(1000, self.show_crash_message, error_msg)
            return False
        elif random.random() < 0.6:  # 30% chance of annoying message
            annoyance_msg = random.choice(self.annoying_messages)
            self.status_var.set(f"ANNOYANCE: {annoyance_msg}")
        return True
        
    def show_crash_message(self, msg):
        crash_window = tk.Toplevel(self.root)
        crash_window.title("CRASH REPORT")
        crash_window.geometry("500x300")
        crash_window.configure(bg="#1a1a1a")
        
        text = tk.Text(
            crash_window,
            bg="#1a1a1a",
            fg="#ff6b6b",
            font=("Courier", 10),
            wrap=tk.WORD
        )
        text.insert(tk.END, msg)
        text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        close_button = tk.Button(
            crash_window,
            text="CLOSE",
            bg="#ff6b6b",
            fg="white",
            command=crash_window.destroy
        )
        close_button.pack(pady=5)
        
    def clear_all(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)
            cell.config(bg=self.cell_bg)
        self.status_var.set("All cells cleared. Reset to fresh state.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GrittyCalculator(root)
    
    # Make sure we have a valid window
    root.mainloop()