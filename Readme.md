# Jarvis Voice Assistant

This is a Python-based voice assistant project named Jarvis. It is designed to recognize voice commands, perform various tasks like opening websites, playing songs, and adding songs to a Spotify library, as well as interacting with different applications installed on your system. The assistant uses the `speech_recognition` library to process spoken commands and `pyttsx3` for text-to-speech functionality.

## Features
- **Voice Command Recognition:** Detects voice input using `speech_recognition`.
- **Web Navigation:** Can open popular websites such as Google, Facebook, YouTube, etc.
- **Application Control:** Opens locally installed applications like Valorant, WhatsApp, Notion, Calculator, and Notepad.
- **Spotify Integration:**
  - Play music from a local library.
  - Search for songs on Spotify and play them.
  - Add songs to your Spotify "Liked Songs" using voice commands.
- **Text-to-Speech Response:** Uses `pyttsx3` to respond to user commands.

## Prerequisites
To use this project, you'll need the following libraries installed:

```bash
pip install speechrecognition pyttsx3 spotipy requests beautifulsoup4
Additionally, configure your Spotify Developer Application to obtain the necessary credentials for Spotify API integration:

client_id
client_secret
redirect_uri
You will also need to configure OAuth scopes for Spotify:
scope = [
    "user-library-read", 
    "playlist-modify-public", 
    "user-library-modify", 
    "playlist-modify-private"
]
Usage
Initialize Jarvis: The assistant starts by greeting the user.
Listening for Commands: It continuously listens for the activation word ("Jarvis") and processes commands when spoken.
Supported Commands:
Open Websites: Say open google, open youtube, open facebook, etc.
Open Applications: Say open calculator, open notepad, open WhatsApp, etc.
Play Music: Say play song_name to play music either from your local music library or search and play via Spotify.
Add to Liked Songs: Say add song_name to my liked songs to add the song to your Spotify liked songs.
Termination: Say stop to stop the assistant.
Example Commands:
"Jarvis, open Google."
"Jarvis, play Blinding Lights."
"Jarvis, add Levitating to my liked songs."
Spotify Integration
To enable Spotify functionality, follow these steps:

Set up a Spotify Developer account and create an app.
Use the client_id, client_secret, and redirect_uri in the Spotify OAuth setup.
Jarvis uses spotipy to interact with the Spotify API for playing and adding songs.
Troubleshooting
Microphone Issues: Ensure that your microphone is working correctly and configured properly in your system.
Spotify API Errors: Verify that your Spotify credentials are correct and that you've provided the necessary permissions.
Application Paths: If an application fails to open, ensure that the file paths specified in the code are correct for your system.
Future Enhancements
Add support for more applications and voice commands.
Extend functionality to control smart home devices.
Add natural language processing for more complex commands.
License
This project is licensed under the MIT License.

This `README.md` file explains the purpose of your project, its key features, setup instructions, usage examples, and troubleshooting tips. It provides users with a clear understanding of how to run and interact with your voice assistant.
