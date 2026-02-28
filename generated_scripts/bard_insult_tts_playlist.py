#!/usr/bin/env python3
"""
Shakespearean Insult TTS bot for a Spotify playlist.

Requirements (install with pip):
    pip install spotipy pyttsx3
"""

import sys
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pyttsx3

# ------------------- CONFIGURATION -------------------
# Replace these with your own Spotify developer credentials.
SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"

# The script expects a Spotify playlist URI or URL as the first command‑line argument.
# Example:
#   python insult_tts_playlist.py https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO
# ------------------- END CONFIGURATION -------------------

# Shakespearean insults (feel free to expand)
INSULTS = [
    "cankerous", "cavil", "cocker", "dankish", "fool", "glistering‑gudgeon",
    "incontinent", "jaded", "lewd", "muddy‑minded", "obsequious", "pacock",
    "pestilent", "pox‑scarred", "quailing", "rascally", "reprehensible",
    "sl Springe", "spongy", "timorous", "wagtail", "wheedle‑wit"
]

def get_insult_for_title(title: str) -> str:
    """Return a Shakespearean insult that references the given title."""
    # Simple heuristic: prefix with a random insult and add a rhyming fragment.
    insult = random.choice(INSULTS)
    rhyme = title.split()[-1] if title.split() else "song"
    return f"Thou art a {insult} of {rhyme}!"

def init_spotify():
    """Create and return an authenticated Spotipy client."""
    creds = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                     client_secret=SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials_manager(creds))
    return sp

def fetch_playlist_tracks(sp, playlist_uri: str):
    """Yield track names from the given playlist URI."""
    # Resolve the playlist URI to a playlist object
    playlist = sp.playlist(playlist_uri)
    offset = 0
    limit = 100
    while True:
        results = sp.playlist_items(playlist_uri, offset=offset, limit=limit)
        for item in results["items"]:
            if item["track"]:
                yield item["track"]["name"]
        offset += limit
        if offset >= results["total"]:
            break

def init_tts_engine():
    """Initialize pyttsx3 engine (offline TTS)."""
    engine = pyttsx3.init()
    # Optional: adjust rate/volume/voice
    engine.setProperty('rate', 150)
    return engine

def speak(engine, text: str):
    """Speak the given text using the provided engine."""
    engine.say(text)
    engine.runAndWait()

def main():
    if len(sys.argv) < 2:
        print("Usage: python insult_tts_playlist.py <playlist_uri_or_url>")
        sys.exit(1)

    playlist_input = sys.argv[1]
    # Convert URL to URI if needed
    if playlist_input.startswith("http"):
        sp = init_spotify()
        # Spotify URI format: spotify:playlist:<id>
        # Extract ID from URL and build URI
        import urllib.parse
        parsed = urllib.parse.urlparse(playlist_input)
        playlist_id = urllib.parse.parse_qs(parsed.query).get("playlist", [None])[0]
        if not playlist_id:
            playlist_id = parsed.path.split("/")[-1]
        playlist_uri = f"spotify:playlist:{playlist_id}"
    else:
        playlist_uri = playlist_input

    # Initialize Spotify and TTS
    sp = init_spotify()
    engine = init_tts_engine()

    print("Gathering playlist tracks...")
    for title in fetch_playlist_tracks(sp, playlist_uri):
        insult_sentence = get_insult_for_title(title)
        print(f"Speaking: {insult_sentence}")
        speak(engine, insult_sentence)

if __name__ == "__main__":
    main()