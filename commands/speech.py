import pyttsx3
import os

class speech:
    def __init__(self):
        # Initialize pyttsx3 and set properties
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    def create_speech_output(self, text):
        """
        Generates a speech output from the given text and saves it to an output file.
        Args:
            text (str): The text to be converted to speech.
        """
        
        self.engine.save_to_file(text, "output.wav")
        self.engine.runAndWait()