#!/usr/bin/env python3
"""
Replace every occurrence of “Monday” with “Coffee‑day” in a text file and email the result.
Usage: python3 coffee_day_email.py <input_file> <recipient_email>
"""

import sys
import os
import smtplib
from email.message import EmailMessage

def replace_text(text: str) -> str:
    return text.replace("Monday", "Coffee‑day")

def send_email(content: str, recipient: str, sender: str, password: str, subject: str = "Coffee‑day Update"):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(content)

    # Use SMTP (Adjust server/port as needed, e.g., Gmail: smtp.gmail.com:587)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 coffee_day_email.py <input_file> <recipient_email>")
        sys.exit(1)

    input_path = sys.argv[1]
    recipient = sys.argv[2]

    if not os.path.isfile(input_path):
        print(f"Error: file '{input_path}' does not exist.")
        sys.exit(1)

    # ----- Read and replace -----
    with open(input_path, "r", encoding="utf-8") as f:
        original = f.read()
    modified = replace_text(original)

    # ----- Email credentials (replace with real values) -----
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_app_password"   # Use an app‑specific password if 2‑FA enabled

    # ----- Send email -----
    try:
        send_email(modified, recipient, SENDER_EMAIL, SENDER_PASSWORD)
        print(f"Email sent to {recipient}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    main()