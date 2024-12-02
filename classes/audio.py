import constants as constant
import pyaudio
import wave

class AudioPlayer:
    def play_audio(audio_path, audio_device_index=constant.AUDIO_OUTPUT_INDEX, chunk=1024):
        """
        Play an audio file using the specified audio device.
        Args:
            audio_path (str): The path to the audio file to be played.
            audio_device_index (int, optional): The index of the audio output device. Defaults to constant.AUDIO_OUTPUT_INDEX.
            chunk (int, optional): The size of the audio chunks to read and play at a time. Defaults to 1024.
        Returns:
            None
        """

        wf = wave.open(audio_path, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        output_device_index=audio_device_index)

        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()