import pyttsx3
import re

def is_hinglish(text):
    # A simple check for Hindi words in the text
    hindi_words = re.compile(r'[अ-ह]+')  # Regex to find Hindi characters
    return bool(hindi_words.search(text))

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 1)  # Volume 0-1

    # Speak the text
    engine.say(text)
    
    # Wait until speaking is finished
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech (English or Hinglish): ")
    
    if is_hinglish(text):
        print("Detected Hinglish input.")
    else:
        print("Detected English input.")
    
    text_to_speech(text)