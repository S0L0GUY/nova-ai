from classes.audio import AudioPlayer
import constants as constant
import edge_tts
import os

class TextToSpeech:
    @staticmethod
    def create_tts_output(text):
        """
        Generates a text-to-speech (TTS) output file from the given text.
        Args:
            text (str): The input text to be converted to speech.
        Returns:
            None
        The function creates an MP3 file with the speech synthesis of the input text.
        The filename is derived from the first 10 characters of the text, with spaces replaced by underscores.
        The output file is saved in the directory specified by `constant.TTS_OUTPUT_DIR`.
        """

        output_dir = constant.TTS_OUTPUT_DIR
        communicator = edge_tts.Communicator()
        filename = f"{text[:10].replace(' ', '_')}.mp3"
        output_path = os.path.join(output_dir, filename)
        communicator.synthesize_to_file(text, output_path)

    @staticmethod
    def play_tts(text):
        """
        Plays text-to-speech (TTS) audio for the given text.
        This function attempts to play a pre-generated TTS audio file for the given text.
        If the audio file does not exist, it generates the TTS audio and then plays it.
        Args:
            text (str): The text to be converted to speech and played.
        Raises:
            Exception: If there is an error in playing or generating the TTS audio.
        """

        try:
            AudioPlayer.play_audio(f"{text[:10].replace(' ', '_')}.mp3")
        except:
            TextToSpeech.create_tts_output(text)
            AudioPlayer.play_audio(f"{text[:10].replace(' ', '_')}.mp3")