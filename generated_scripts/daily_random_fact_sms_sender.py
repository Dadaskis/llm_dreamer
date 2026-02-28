import random
import schedule
import time
import datetime
import os
from twilio.rest import Client

# ================== Config ==================
# Replace with your Twilio credentials or set as environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "YOUR_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "YOUR_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER", "+1234567890")  # Your Twilio phone number
RECIPIENT_NUMBER = os.getenv("SMS_TO_NUMBER", "+0987654321")          # Destination phone number
# ================== Fun facts ==================
FUN_FACTS = [
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.",
    "A day on Venus is longer than a year on Venus.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can be 15 cm taller during a hot summer day.",
    "Bananas are berries, but strawberries aren't.",
    "A bolt of lightning is five times hotter than the surface of the Sun.",
    "Wombat poop is cube‑shaped.",
    "There are more possible games of chess than atoms in the observable universe."
]

# ================== Twilio client setup ==================
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_random_fact():
    """Select a random fun fact and send it via SMS."""
    fact = random.choice(FUN_FACTS)
    try:
        message = client.messages.create(
            body=fact,
            from_=TWILIO_FROM_NUMBER,
            to=RECIPIENT_NUMBER
        )
        print(f"[{datetime.datetime.now()}] Sent SMS (sid: {message.sid})")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Failed to send SMS: {e}")

def schedule_job():
    """Schedule the SMS to be sent every Monday at 09:00."""
    schedule.every().monday.at("09:00").do(send_random_fact)

    print("Scheduler started. Waiting for 9 AM Monday... (will run indefinitely)")
    while True:
        schedule.run_pending()
        time.sleep(30)  # check twice a minute

if __name__ == "__main__":
    schedule_job()