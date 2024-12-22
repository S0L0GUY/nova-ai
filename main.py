from classes.whisper import WhisperTranscriber
from classes.system_prompt import SystemPrompt
from classes.json_wrapper import JsonWrapper
from classes.tts import TextToSpeech
from classes.osc import VRChatOSC
import constants as constant
from openai import OpenAI
import datetime
import http_server
import re

# pip install edge-tts

osc = VRChatOSC()
transcriber = WhisperTranscriber()

# Send message to VRChat to indicate that the system is starting
osc.send_message("System Loading")
osc.set_typing_indicator(True)

# Get the system prompt
system_prompt = SystemPrompt.get_full_prompt("normal")

# Set up history
now = datetime.datetime.now()

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

def find_matching_words(word_list, string_to_check):
    """
    Args:
        word_list (list): All of the words that you want to detect.
        string_to_check (): The string that you want to parse for words.

    Returns:
        boolean: Is there a word from the list in the string to check?

    Parse the string to check for words in the list.
    """    
    return [word for word in word_list if word in string_to_check]

# Main logic
while True:
    # Creates model parameters
    completion = openai_client.chat.completions.create(
        model=constant.MODEL_ID,
        messages=history,
        temperature=constant.LM_TEMPERATURE,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}

    osc.send_message("Thinking")
    osc.set_typing_indicator(True)

    buffer = ""
    full_response = ""

    for chunk in completion:
        osc.set_typing_indicator(True)
        if chunk.choices[0].delta.content:
            buffer += chunk.choices[0].delta.content
            sentence_chunks = chunk_text(buffer)
            while len(sentence_chunks) > 1:
                sentence = sentence_chunks.pop(0)
                full_response += f" {sentence}"
                print(f"AI: {sentence}")
                TextToSpeech.play(sentence)
                osc.send_message(sentence)
            buffer = sentence_chunks[0]

    if buffer:
        osc.set_typing_indicator(True)
        full_response += f" {buffer}"
        print(f"AI: {buffer}")
        TextToSpeech.play(buffer)
        osc.send_message(sentence)
        new_message["content"] = full_response

    osc.set_typing_indicator(False)

    JsonWrapper.write_json(constant.HISTORY_PATH, new_message)

    # Get user speech input
    user_speech = ""

    while not user_speech:
        user_speech = transcriber.get_speech_input()

    f"HUMAN: {user_speech}"

    JsonWrapper.write_json(constant.HISTORY_PATH, user_speech)