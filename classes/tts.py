import constants as constant
import edge_tts
import os

class TextToSpeech:
    async def generate_speech(text):
        """
        Asynchronously generates speech from the given text and saves it as an MP3 file.
        Args:
            text (str): The text to be converted to speech.
        Returns:
            None
        """
        if not os.path.exists(f"{constant.TTS_OUTPUT_DIR}/{text}.mp3"):
            communicate = edge_tts.Communicate(text, constant.TTS_VOICE)
            await communicate.save(f"{constant.TTS_OUTPUT_DIR}/{text}.mp3")