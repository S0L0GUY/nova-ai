import constants as constant
import whisper
import pyaudio
import numpy as np
import threading

transcription_result = ""

class WhisperTranscriber:
    def __init__(self, device_index=constant.AUDIO_INPUT_INDEX, rate=16000, chunk_size=1024):
        self.device_index = device_index
        self.rate = rate
        self.chunk_size = chunk_size
        self.model = whisper.load_model("base")
        self.audio_interface = pyaudio.PyAudio()
        self.stream = self.audio_interface.open(format=pyaudio.paInt16,
                                                channels=1,
                                                rate=self.rate,
                                                input=True,
                                                input_device_index=self.device_index,
                                                frames_per_buffer=self.chunk_size)
    
    def transcribe(self):
        """
        Transcribes audio data from the stream in real-time.
        This method continuously reads audio data from the stream, processes it,
        and uses the model to transcribe the audio into text. The transcription
        result is stored in the global variable `transcription_result` and printed
        to the console.
        Attributes:
            transcription_result (str): The transcribed text from the audio data.
        """

        global transcription_result
        print("Recording...")
        frames = []
        while True:
            data = self.stream.read(self.chunk_size)
            frames.append(np.frombuffer(data, dtype=np.int16))
            audio_data = np.concatenate(frames, axis=0).astype(np.float32) / 32768.0
            result = self.model.transcribe(audio_data)
            transcription_result = result['text']

    def start_transcription(self):
        """
        Starts the transcription process in a separate daemon thread.
        This method initializes a new thread to run the `transcribe` method, allowing
        the transcription process to run in the background without blocking the main thread.
        The thread is set as a daemon, meaning it will automatically close when the main
        program exits.
        """

        transcription_thread = threading.Thread(target=self.transcribe)
        transcription_thread.daemon = True
        transcription_thread.start()

    def stop_transcription(self):
        """
        Stops the audio transcription process by stopping the audio stream,
        closing it, and terminating the audio interface.
        This method performs the following actions:
        1. Stops the audio stream.
        2. Closes the audio stream.
        3. Terminates the audio interface.
        Raises:
            Exception: If there is an issue stopping the stream or terminating the audio interface.
        """

        self.stream.stop_stream()
        self.stream.close()
        self.audio_interface.terminate()