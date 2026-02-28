import tkinter as tk
from tkinter import ttk
import random

class SurrealWeatherGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Surreal Weather Report Generator")
        self.root.geometry("500x400")
        self.root.configure(bg="#87CEEB")
        
        # Create main frame
        main_frame = tk.Frame(root, bg="#87CEEB")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Surreal Weather Report Generator", 
            font=("Arial", 18, "bold"),
            bg="#87CEEB",
            fg="#2F4F4F"
        )
        title_label.pack(pady=(0, 20))
        
        # Forecast display
        self.forecast_label = tk.Label(
            main_frame,
            text="Click 'Generate Forecast' for surreal weather predictions!",
            font=("Arial", 14),
            bg="#87CEEB",
            fg="#2F4F4F",
            wraplength=450,
            justify=tk.CENTER
        )
        self.forecast_label.pack(pady=20)
        
        # Generate button
        self.generate_button = tk.Button(
            main_frame,
            text="Generate Surreal Forecast",
            font=("Arial", 12, "bold"),
            bg="#4682B4",
            fg="white",
            activebackground="#5A9BD5",
            command=self.generate_forecast,
            padx=20,
            pady=10
        )
        self.generate_button.pack(pady=20)
        
        # Example forecasts
        example_frame = tk.Frame(main_frame, bg="#87CEEB")
        example_frame.pack(pady=20)
        
        example_label = tk.Label(
            example_frame,
            text="Examples of surreal forecasts:",
            font=("Arial", 10, "italic"),
            bg="#87CEEB",
            fg="#2F4F4F"
        )
        example_label.pack()
        
        examples = [
            "Today's weather: 40% chance of having a good day",
            "Tomorrow's forecast: 75% chance of personal transformation",
            "Rain probability: 20% of finding your true purpose",
            "Temperature: 68 degrees Fahrenheit of unexpected joy"
        ]
        
        for example in examples:
            example_text = tk.Label(
                example_frame,
                text=example,
                font=("Arial", 9),
                bg="#87CEEB",
                fg="#556B2F",
                wraplength=450,
                justify=tk.CENTER
            )
            example_text.pack(pady=2)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Made with surreal weather magic ✨",
            font=("Arial", 8),
            bg="#87CEEB",
            fg="#2F4F4F"
        )
        footer_label.pack(side=tk.BOTTOM, pady=10)
    
    def generate_forecast(self):
        # Surreal weather phrases
        phrases = [
            "Today's weather: {chance}% chance of having a good day",
            "Tomorrow's forecast: {chance}% chance of personal transformation",
            "Rain probability: {chance}% of finding your true purpose",
            "Temperature: {temp} degrees Fahrenheit of unexpected joy",
            "Humidity: {chance}% of feeling absolutely magical",
            "Wind speed: {chance}% of being carried away by inspiration",
            "Cloud cover: {chance}% of looking through rose-colored glasses",
            "UV index: {chance}% of glowing from within",
            "Air pressure: {chance}% of feeling like a cosmic breeze",
            "Precipitation: {chance}% of falling into wonder",
            "Fog probability: {chance}% of finding clarity in the mist",
            "Sunshine: {chance}% of feeling like you're making the world brighter"
        ]
        
        # Percent chances
        chances = [random.randint(10, 90) for _ in range(3)]
        
        # Temps
        temps = [random.randint(40, 80) for _ in range(2)]
        
        # Select random phrase
        phrase = random.choice(phrases)
        
        # Format with random values
        forecast = phrase.format(
            chance=random.choice(chances),
            temp=random.choice(temps)
        )
        
        # Update display
        self.forecast_label.config(text=forecast, font=("Arial", 14, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = SurrealWeatherGenerator(root)
    root.mainloop()