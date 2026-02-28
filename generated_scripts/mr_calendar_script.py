#!/usr/bin/env python3
import imaplib
import email
import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import decode_header
import re
import time
import json
import os
from datetime import datetime, timedelta
import calendar as cal
from collections import defaultdict

# ======================
# CONFIGURATION
# ======================
IMAP_SERVER = 'imap.gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
EMAIL_ADDRESS = 'your_email@gmail.com'  # Change this
EMAIL_PASSWORD = 'your_app_password'    # Change this (use app password for Gmail)
STATE_FILE = 'calendar_monitor_state.json'
CHECK_INTERVAL = 60  # seconds

# Passive-aggressive messages (in order of escalation)
MESSAGES = [
    "Just a gentle reminder that the scheduled end time for our meeting was {end_time}. No rush though!",
    "I notice we're running a bit over our scheduled {end_time}. My calendar shows I have another commitment soon, but I'm sure we can wrap up quickly!",
    "It's now {over_minutes} minutes past our scheduled {end_time}. Are we still on track to conclude? I wouldn't want to keep anyone waiting!",
    "We've officially exceeded our scheduled {end_time} by {over_minutes} minutes. My next meeting is starting soon, but I'm happy to stay if everyone else is!",
    "This meeting has been running for {over_minutes} minutes beyond the scheduled {end_time}. I'm going to have to leave at {leave_time} for my next appointment, but feel free to continue without me!",
    "This meeting has overrun by {over_minutes} minutes past {end_time}. I'm going to assume we're finished since my calendar says we should have ended {over_minutes} minutes ago. Have a great day!",
    "Automated notification: Meeting {over_minutes} minutes over scheduled end. Please respect everyone's time in future meetings."
]

# ======================
# STATE MANAGEMENT
# ======================
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

# ======================
# ICAL PARSING (Simplified)
# ======================
def parse_ical_event(ical_str):
    """Parse iCal string to extract event details. Simplified for common patterns."""
    event = {}
    lines = ical_str.split('\r\n') if '\r\n' in ical_str else ical_str.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('UID:'):
            event['uid'] = line[4:]
        elif line.startswith('DTSTART:'):
            event['start'] = parse_dt(line[7:])
        elif line.startswith('DTEND:'):
            event['end'] = parse_dt(line[6:])
        elif line.startswith('ORGANIZER'):
            # Extract email from ORGANIZER;CN=Name:mailto:email@domain.com
            match = re.search(r'mailto:([^;\r\n]+)', line)
            if match:
                event['organizer'] = match.group(1)
        elif line.startswith('SUMMARY:'):
            event['summary'] = line[8:]
        elif line.startswith('DESCRIPTION:'):
            event['description'] = line[12:]
    
    return event if 'uid' in event and 'end' in event else None

def parse_dt(dt_str):
    """Parse iCal datetime string. Handles UTC (Z) and basic formats."""
    # Remove Z (UTC) indicator if present
    dt_str = dt_str.rstrip('Z')
    
    # Try different formats
    formats = [
        '%Y%m%dT%H%M%S',    # 20231201T143000
        '%Y%m%dT%H%M%S%f',  # With microseconds
        '%Y-%m-%d %H:%M:%S', # Fallback
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(dt_str, fmt)
        except ValueError:
            continue
    
    # Default fallback
    return datetime.now()

# ======================
# EMAIL OPERATIONS
# ======================
def send_passive_aggressive_email(to_email, event_summary, scheduled_end, over_minutes, leave_time=None):
    """Send increasingly passive-aggressive email."""
    index = min(over_minutes // 5, len(MESSAGES) - 1)  # Escalate every 5 minutes
    message_template = MESSAGES[index]
    
    # Format message with event details
    message = message_template.format(
        end_time=scheduled_end.strftime('%I:%M %p'),
        over_minutes=over_minutes,
        leave_time=(leave_time or (scheduled_end + timedelta(minutes=over_minutes + 10))).strftime('%I:%M %p')
    )
    
    subject = f"Re: {event_summary} - Meeting Time"
    body = f"Hello,\n\n{message}\n\nBest regards,\nYour Calendar Assistant"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, 465, context=context) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Sent email to {to_email} (over by {over_minutes} mins)")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

# ======================
# MAIN MONITOR LOOP
# ======================
def monitor_calendar():
    state = load_state()
    
    while True:
        try:
            current_time = datetime.now()
            print(f"\n[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] Checking calendar...")
            
            # Connect to IMAP
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            mail.select('inbox')
            
            # Search for recent emails with calendar invites (last 7 days)
            since_date = (current_time - timedelta(days=7)).strftime('%d-%b-%Y')
            status, messages = mail.search(None, f'(SINCE "{since_date}")')
            
            if status != 'OK':
                print("No messages found or search failed")
                mail.logout()
                time.sleep(CHECK_INTERVAL)
                continue
            
            processed_uids = set()
            
            for num in messages[0].split():
                status, data = mail.fetch(num, '(RFC822)')
                if status != 'OK':
                    continue
                
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                # Get UID for deduplication
                msg_uid = msg.get('Message-ID', '')
                if msg_uid in processed_uids:
                    continue
                processed_uids.add(msg_uid)
                
                # Check for calendar attachments
                for part in msg.walk():
                    if part.get_content_type() == 'text/calendar':
                        ical_data = part.get_payload(decode=True)
                        if ical_data:
                            try:
                                ical_str = ical_data.decode('utf-8')
                            except UnicodeDecodeError:
                                ical_str = ical_data.decode('latin-1')
                            
                            event = parse_ical_event(ical_str)
                            if event:
                                uid = event['uid']
                                event_end = event['end']
                                
                                # Only process events ending in the past 24 hours or upcoming 24 hours
                                if not (current_time - timedelta(hours=24) <= event_end <= current_time + timedelta(hours=24)):
                                    continue
                                
                                # Update state with latest event info
                                if uid not in state or state[uid]['end'] != event_end.isoformat():
                                    state[uid] = {
                                        'end': event_end.isoformat(),
                                        'summary': event.get('summary', 'Meeting'),
                                        'organizer': event.get('organizer', EMAIL_ADDRESS),
                                        'last_notified': None,
                                        'notifications_sent': 0
                                    }
                                    print(f"Tracking event: {event.get('summary')} ending {event_end}")
            
            mail.logout()
            
            # Check for overdue meetings
            uids_to_remove = []
            for uid, event_data in state.items():
                event_end = datetime.fromisoformat(event_data['end'])
                organizer = event_data['organizer']
                summary = event_data['summary']
                
                # Skip if organizer is our own email (don't email ourselves)
                if organizer.lower() == EMAIL_ADDRESS.lower():
                    continue
                
                # Check if meeting is over
                if current_time > event_end:
                    over_minutes = int((current_time - event_end).total_seconds() / 60)
                    
                    # Check if we should send notification (every 5 minutes, up to limit)
                    last_notified = event_data.get('last_notified')
                    notifications_sent = event_data.get('notifications_sent', 0)
                    
                    should_notify = False
                    if last_notified:
                        last_time = datetime.fromisoformat(last_notified)
                        if current_time - last_time >= timedelta(minutes=5):
                            should_notify = True
                    else:
                        # First notification after 5 minutes over
                        if over_minutes >= 5:
                            should_notify = True
                    
                    if should_notify and notifications_sent < 10:  # Max 10 notifications
                        if send_passive_aggressive_email(
                            organizer, 
                            summary, 
                            event_end, 
                            over_minutes,
                            event_end + timedelta(minutes=over_minutes + 15)
                        ):
                            state[uid]['last_notified'] = current_time.isoformat()
                            state[uid]['notifications_sent'] = notifications_sent + 1
                
                # Clean up old events (older than 48 hours after end)
                if current_time - event_end > timedelta(hours=48):
                    uids_to_remove.append(uid)
            
            # Remove old events
            for uid in uids_to_remove:
                del state[uid]
            
            save_state(state)
            
        except Exception as e:
            print(f"Error in monitoring loop: {e}")
        
        time.sleep(CHECK_INTERVAL)

# ======================
# ENTRY POINT
# ======================
if __name__ == "__main__":
    print("Calendar Monitor Started")
    print(f"Checking every {CHECK_INTERVAL} seconds")
    print("Press Ctrl+C to stop\n")
    
    try:
        monitor_calendar()
    except KeyboardInterrupt:
        print("\nMonitor stopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")