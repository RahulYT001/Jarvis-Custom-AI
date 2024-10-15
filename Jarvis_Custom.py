import speech_recognition as sr
import pyttsx3
import webbrowser
import Music_library
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
from bs4 import BeautifulSoup
import subprocess

def call(path):
    subprocess.call(path)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def processCommand(command):
    """Processes the spoken command and performs the corresponding action."""
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open valorant" in command:
        try:
            subprocess.Popen([r"c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\Valorant.lnk"])
        except Exception as e:
            print(f"Error opening Valorant: {e}")
            speak("Sorry, there was an error opening Valorant.")
    # elif "open discord" in command:
    #     try:
    #         call(path)
    #     except Exception as e:
    #         print(f"Error opening Discord: {e}")
    #         speak("Sorry, there was an error opening Discord.")
    elif "open whatsapp" in command:
        try:
            call("Whatsapp")
        except Exception as e:
            print(f"Error opening WhatsApp: {e}")
            speak("Sorry, there was an error opening WhatsApp.")
    elif "open notion" in command:
        try:
            call(r"c:\Users\ranar\AppData\Local\Programs\Notion\Notion.exe")
        except Exception as e:
            print(f"Error opening Notion: {e}")
            speak("Sorry, there was an error opening Notion.")
    elif "open calculator" in command:
        try:
            call("Calculator")
        except Exception as e:
            print(f"Error opening Calculator: {e}")
            speak("Sorry, there was an error opening Calculator.")
    elif "open notepad" in command:
        try:
            call("Notepad")
        except Exception as e:
            print(f"Error opening Notepad: {e}")
            speak("Sorry, there was an error opening Notepad.")

#Playing from library then from spotify if not found!

    elif command.startswith("play"):
        song = command.split("play", 1)[1].strip()
        print(f"Extracted song: {song}")  # Debugging print statement
        
        if song in Music_library.music:
            link = Music_library.music[song]
            webbrowser.open(link)

        else:
            song_url, _ = search_song_spotify(song)
            if song_url:
                speak(f"Opening {song}.")
                webbrowser.open(song_url)
            else:
                speak(f"Sorry, I couldn't find the song {song}.")
                print(f"Song {song} not found on Spotify.")  # Debugging print statement
#Adding to my liked songs on spotify

    elif command.startswith("add") and "to my liked songs" in command:
        song = command.split("add", 1)[1].split("to my liked songs")[0].strip()
        print(f"Adding song: {song}")  # Debugging print statement
        
        _, song_id = search_song_spotify(song)
        if song_id:
            add_song_to_liked(song_id)
            speak(f"Added {song} to your liked songs.")
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
            print(f"Song {song} not found on Spotify.")  # Debugging print statement



def search_song_spotify(song_name):
    """Search for a song on Spotify and return its URL and ID."""
    results = sp.search(q=song_name, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        track = tracks[0]
        # Return the URL and ID of the track
        return track['external_urls']['spotify'], track['id']
    return None, None


def add_song_to_liked(song_id):
    """Add a song to the user's liked songs on Spotify."""
    try:
        sp.current_user_saved_tracks_add([song_id])
        speak("Song has been added to your liked songs.")
        print(f"Added song with ID {song_id} to liked songs.")
    except Exception as e:
        speak("There was an error adding the song to your liked songs.")
        print(f"Error adding song to liked songs: {e}")

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen(recognizer, source):
    """Listens for speech and converts it to text."""
    text = ""
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start.")
        speak("Listening timed out. Please try again.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
        speak("Sorry, there was an error processing your request.")
    return text


# Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="",
    client_secret="",
    redirect_uri="http://localhost:8888/callback",
    scope=["user-library-read", "playlist-modify-public", "user-library-modify", "playlist-modify-private"]
))

if __name__ == "__main__":
    speak("Initializing Jarvis, welcome sir")
    
    recognizer = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                command = listen(recognizer, source)
                
                if "jarvis" in command.lower():
                    speak("Yes?")
                    print("Jarvis Active...")
                    
                    with sr.Microphone() as source:
                        command = listen(recognizer, source)
                        if "stop" in command.lower():
                            speak("Goodbye sir.")
                            print("Stopping Jarvis...")
                            break
                        processCommand(command)
        except KeyboardInterrupt:
            print("Program terminated by user.")
            speak("Goodbye, sir.")
            break
        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred. Please try again.")
