import constants as constant
import edge_tts
import pyaudio

class TextToSpeech:
    def __init__(self, text, audio_device_index=constant.AUDIO_OUTPUT_INDEX, voice=None):
        self.text = text
        self.audio_device_index = audio_device_index
        self.voice = voice if voice else "en-US-JennyNeural"
        self.tts = edge_tts.Communicate()

    async def play(self):
        """
        Asynchronously plays the synthesized text-to-speech audio.
        This method synthesizes the text using the specified voice and plays the resulting audio stream through the selected audio output device.
        Args:
            None
        Returns:
            None
        Raises:
            Exception: If there is an error during the synthesis or playback process.
        """
        stream = await self.tts.synthesize(self.text, self.voice)
        audio = pyaudio.PyAudio()
        stream_out = audio.open(format=audio.get_format_from_width(2),
                                channels=1,
                                rate=24000,
                                output=True,
                                output_device_index=self.audio_device_index)
        stream_out.write(stream)
        stream_out.stop_stream()
        stream_out.close()
        audio.terminate()