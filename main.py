from classes.whisper import WhisperTranscriber
from classes.system_prompt import SystemPrompt
from classes.json_wrapper import JsonWrapper
from classes.audio import AudioPlayer
from classes.osc import VRChatOSC
from openai import OpenAI
import datetime
import http_server
import threading
import re

# pip install edge-tts

osc = VRChatOSC()
transcriber = WhisperTranscriber()

# Send message to VRChat to indicate that the system is starting
osc.send_message("System Loading")
osc.set_typing_indicator(True)

# Set up the transcription thread
transcriber.start_transcription()

# Get the system prompt
mood = JsonWrapper.read_json("mood.json")["mood"]
system_prompt = SystemPrompt.get_full_prompt(mood)

# Set up history
now = datetime.now()

history = [
    {"role": "system", "content": system_prompt},
    {"role": "system", "content": f"Today is {now.strftime("%Y-%m-%d")}"},
    {"role": "user", "content": "Hey"},
]

# Set up LLM
openai_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def chunk_text(text):
    """
    Args:
        text (string): The text to break down.

    Returns:
        string: Text chunk.

    Split the text by sentence-ending punctuation
    """    
    chunks = re.split(r'(?<=[.,;:!?]) +', text)
    return chunks

# Place ~NOVA~ *OPTIONAL*

# Main logic
while True:
    pass