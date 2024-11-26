from translate import Translator
import pyttsx3

class translate:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

    def translate_text(self, text):
        """
        Args:
            text (string): The text that you want to translate.

        Returns:
            string: The translated text.

        Take text and translate it based on language.txt
        """

        with open('variable/language.txt', 'r') as file:
            language = file.read()

        translator = Translator(to_lang=language)

        if language == "en": # English
            for voice in self.voices:
                # Set the voice to Zira for pyttsx3
                if "Zira" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        elif language == "de": # German
            for voice in self.voices:
                # Set the voice to Hedda for pyttsx3
                if "Hedda" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        elif language == "fr": # French
            for voice in self.voices:
                # Set the voice to Hortense for pyttsx3
                if "Hortense" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        elif language == "it": # Italian
            for voice in self.voices:
                # Set the voice to Elsa for pyttsx3
                if "Elsa" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        elif language == "pt-BR": # VRC_PORTuguese
            for voice in self.voices:
                # Set the voice to Maria for pyttsx3
                if "Maria" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        elif language == "es": # Spanish
            for voice in self.voices:
                # Set the voice to Sabina for pyttsx3
                if "Sabina" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        elif language == 'ko': # Korean
            for voice in self.voices:
                # Set the voice to Heami for pyttsx3
                if "Heami" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        else:
            for voice in self.voices:
                # Set the voice to Zira for pyttsx3
                if "Zira" in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break

        return translator.translate(text)
