import variable.constants as constant
import pyaudio
import wave
import os

class audio:
    def __init__(self):
        pass
    
    def play_audio_file(file_path, output_device_index=constant.AUDIO_OUTPUT_INDEX, delete_after_play=False):
        """
        Plays an audio file using the specified output device.
        Args:
            file_path (str): The path to the audio file to be played.
            output_device_index (int, optional): The index of the output device to use for playback. Defaults to constant.AUDIO_OUTPUT_INDEX.
            delete_after_play (bool, optional): If True, deletes the audio file after playback. Defaults to False.
        Raises:
            FileNotFoundError: If the specified audio file does not exist.
            OSError: If there is an error opening or reading the audio file.
        """
        
        wf = wave.open(file_path, 'rb')
        p = pyaudio.PyAudio()

        # Open the audio stream
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
            output_device_index=output_device_index
        )

        # Read and play audio data
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Cleanup
        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()
        
        if delete_after_play:
            os.remove(file_path)
