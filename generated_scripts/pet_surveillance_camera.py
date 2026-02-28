import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import smtplib
import threading
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os
import numpy as np
import subprocess
import sys

class DarkPetCamera:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Surveillance Camera")
        self.root.geometry("500x600")
        self.root.configure(bg="#1a1a1a")
        
        # Dark theme styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#1a1a1a')
        style.configure('TLabel', background='#1a1a1a', foreground='#e0e0e0')
        style.configure('TButton', background='#333333', foreground='#ffffff')
        style.map('TButton', background=[('active', '#444444')])
        
        # Camera and email settings
        self.camera_index = 0
        self.is_recording = False
        self.capture_thread = None
        self.email_config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'email': '',
            'password': '',
            'recipient': ''
        }
        
        # Create UI
        self.create_widgets()
        
        # Initialize camera
        self.setup_camera()
        
    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, padx=20, pady=10)
        
        header_label = ttk.Label(header_frame, text="PET SURVEILLANCE CAMERA", font=('Arial', 16, 'bold'))
        header_label.pack()
        
        # Camera preview
        self.preview_frame = ttk.Frame(self.root, height=200)
        self.preview_frame.pack(fill=tk.X, padx=20, pady=10)
        self.preview_label = ttk.Label(self.preview_frame, text="Camera Preview")
        self.preview_label.pack(expand=True)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(self.root, text="Settings", padding=10)
        settings_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Email settings
        ttk.Label(settings_frame, text="SMTP Server:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.smtp_entry = ttk.Entry(settings_frame, width=30)
        self.smtp_entry.grid(row=0, column=1, pady=2, padx=5)
        self.smtp_entry.insert(0, "smtp.gmail.com")
        
        ttk.Label(settings_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.email_entry = ttk.Entry(settings_frame, width=30)
        self.email_entry.grid(row=1, column=1, pady=2, padx=5)
        
        ttk.Label(settings_frame, text="Password:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.password_entry = ttk.Entry(settings_frame, width=30, show="*")
        self.password_entry.grid(row=2, column=1, pady=2, padx=5)
        
        ttk.Label(settings_frame, text="Recipient:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.recipient_entry = ttk.Entry(settings_frame, width=30)
        self.recipient_entry.grid(row=3, column=1, pady=2, padx=5)
        
        # Camera settings
        ttk.Label(settings_frame, text="Camera Index:").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.camera_entry = ttk.Entry(settings_frame, width=10)
        self.camera_entry.grid(row=4, column=1, sticky=tk.W, pady=2, padx=5)
        self.camera_entry.insert(0, "0")
        
        # Control buttons
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.start_button = ttk.Button(control_frame, text="Start Recording", command=self.start_recording)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(control_frame, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.test_button = ttk.Button(control_frame, text="Send Test Email", command=self.send_test_email)
        self.test_button.pack(side=tk.LEFT, padx=5)
        
        # Status text
        self.status_text = tk.Text(self.root, height=10, width=60, bg="#2d2d2d", fg="#ffffff", insertbackground="#ffffff")
        self.status_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Automatically check for camera
        self.root.after(1000, self.check_camera)
        
    def setup_camera(self):
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.log_message("Error: Could not open camera")
                self.status_var.set("Camera Error")
            else:
                self.status_var.set("Camera Ready")
        except Exception as e:
            self.log_message(f"Camera setup error: {e}")
            self.status_var.set("Camera Error")
            
    def check_camera(self):
        if not hasattr(self, 'cap'):
            self.setup_camera()
        elif not self.cap.isOpened():
            self.log_message("Camera disconnected. Attempting to reconnect...")
            self.cap.release()
            self.setup_camera()
            
        self.root.after(5000, self.check_camera)
        
    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.status_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.status_text.see(tk.END)
        self.root.update_idletasks()
        
    def start_recording(self):
        try:
            self.camera_index = int(self.camera_entry.get())
            self.email_config['email'] = self.email_entry.get()
            self.email_config['password'] = self.password_entry.get()
            self.email_config['recipient'] = self.recipient_entry.get()
            
            if not all([self.email_config['email'], self.email_config['password'], self.email_config['recipient']]):
                messagebox.showerror("Error", "Please fill in all email fields")
                return
                
            self.is_recording = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_var.set("Recording... (Watching for pets)")
            
            # Start capture thread
            self.capture_thread = threading.Thread(target=self.capture_loop)
            self.capture_thread.daemon = True
            self.capture_thread.start()
            
            self.log_message("Recording started...")
            
        except Exception as e:
            self.log_message(f"Error starting recording: {e}")
            
    def stop_recording(self):
        self.is_recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_var.set("Stopped")
        self.log_message("Recording stopped")
        
    def capture_loop(self):
        # Delay for first capture (higher chance of catching pet)
        time.sleep(3)
        
        while self.is_recording:
            try:
                # Simple motion detection using frame difference
                ret, frame = self.cap.read()
                if not ret:
                    continue
                    
                # Convert to grayscale for motion detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                
                # Simple presence detection algorithm 
                # (using brightness threshold as proxy for pet presence)
                avg_brightness = np.mean(gray)
                
                # If brightness is above threshold, send photo
                if avg_brightness > 80:  # Adjust this value for your lighting
                    # Add timestamp to frame
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    
                    # Save temporary image
                    filename = f"pet_capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                    cv2.imwrite(filename, frame)
                    
                    # Send email
                    self.send_email(filename)
                    
                    # Cleanup
                    os.remove(filename)
                    
                    # Log
                    self.root.after(0, lambda: self.log_message(f"Pet detected! Photo sent to {self.email_config['recipient']}"))
                    
                    # Wait before next capture
                    time.sleep(60)  # Wait 1 minute before next capture
                else:
                    # Small delay between checks
                    time.sleep(5)
                    
            except Exception as e:
                self.root.after(0, lambda: self.log_message(f"Capture error: {e}"))
                time.sleep(5)
                
    def send_email(self, image_path):
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email_config['email']
            msg['To'] = self.email_config['recipient']
            msg['Subject'] = f"Pet Selfie - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            
            # Add body
            body = "Your pet just got a selfie! Check it out below."
            msg.attach(MIMEText(body, 'plain'))
            
            # Add image
            with open(image_path, 'rb') as f:
                img_data = f.read()
            image = MIMEImage(img_data)
            image.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
            msg.attach(image)
            
            # Create SMTP session
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['email'], self.email_config['password'])
            
            # Send email
            text = msg.as_string()
            server.sendmail(self.email_config['email'], self.email_config['recipient'], text)
            server.quit()
            
            self.root.after(0, lambda: self.log_message(f"Email sent successfully"))
            
        except Exception as e:
            self.root.after(0, lambda: self.log_message(f"Email send error: {e}"))
            
    def send_test_email(self):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['email']
            msg['To'] = self.email_config['recipient']
            msg['Subject'] = "Test Pet Camera Email"
            
            body = "This is a test email from your pet surveillance camera."
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['email'], self.email_config['password'])
            server.sendmail(self.email_config['email'], self.email_config['recipient'], msg.as_string())
            server.quit()
            
            messagebox.showinfo("Test Email", "Test email sent successfully!")
            self.log_message("Test email sent successfully")
            
        except Exception as e:
            messagebox.showerror("Test Email Error", f"Failed to send test email: {e}")
            self.log_message(f"Test email failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DarkPetCamera(root)
    root.mainloop()
```

This Python script creates a dark-themed pet surveillance camera that takes photos of pets when they're nearby and emails them to your address. Here's what it does:

1. **Dark/Gritty Interface**: Uses a dark theme with dark gray backgrounds and light text for a moody aesthetic

2. **Pet Detection**: Uses basic image processing to detect pets through brightness thresholds (since detecting actual animals is complex without ML)

3. **Email Functionality**: Sends photos via SMTP to your email, configured through the GUI

4. **Camera Integration**: Uses OpenCV to control the webcam

5. **Automatic Features**:
   - Automatically checks camera connection
   - Sends emails with timestamps
   - Logs all activity to the text window
   - Waits between captures to prevent spam

**Important Notes**:
- Requires OpenCV: `pip install opencv-python`
- For Gmail, you'll need to enable "Less secure app access" or use App Passwords
- The detection is basic (brightness-based) - for actual pet detection, you would need more advanced computer vision
- Designed to run in the background while unsuspecting pet owners look away

**To Use**:
1. Fill in your email settings in the GUI
2. Start recording (it will monitor for pet presence)
3. When a pet is detected, it takes a photo and emails it
4. You can send a test email to verify configuration works
