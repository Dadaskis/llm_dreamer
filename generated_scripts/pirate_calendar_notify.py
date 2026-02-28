import datetime, json, os, sys
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import pyttsx3

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
CRED_FILE = "token.json"
CLIENT_SECRETS = "credentials.json"


def get_calendar_service():
    creds = None
    if os.path.exists(CRED_FILE):
        creds = google.oauth2.credentials.Credentials.from_authorized_user_file(CRED_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(CRED_FILE, "w") as token:
            token.write(creds.to_json())
    return googleapiclient.discovery.build("calendar", "v3", credentials=creds)


def pirate_speak(text):
    replacements = {
        "meeting": "ye pirate rendezvous",
        "agenda": "treasure hunt plan",
        "reminder": "wake yer eyes, ye scallywag!",
        "deadline": "drop anchor, or ye be walkin' the plank!",
        "project": "voyage",
        "conference": "grand galley meeting",
    }
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text.title() + "! Arr!"


def main():
    service = get_calendar_service()
    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    max_time = now + datetime.timedelta(hours=24)

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now.isoformat(),
            timeMax=max_time.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        print("No upcoming meetings, matey.")
        return

    engine = pyttsx3.init()
    engine.setProperty("rate", 140)

    for ev in events[:5]:
        start = ev["start"].get("dateTime", ev["start"].get("date"))
        summary = ev.get("summary", "No title")
        pirate_text = pirates_peak = pirate_speak(f"{pirate_speak(start)}: {summary}")
        print(pirate_text)
        engine.say(pirate_text)

    engine.runAndWait()


if __name__ == "__main__":
    main()