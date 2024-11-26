import commands.system_prompts as system_prompts
import commands.word_parse as word_parse
import commands.translate as translate
import variable.constants as constant
import commands.snapchat as snapchat
import commands.history as history
import commands.speech as speech
import commands.vrchat as vrchat
import commands.audio as audio
from openai import OpenAI
import datetime

# Indicate to the user that the system is loading
vrchat.type_in_chat("System Loading")
vrchat.typing_indicator(True)

# Set up conversation
openai_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
system_prompt = system_prompts.get_system_prompt()
now = datetime.datetime.now()

history.set(
    [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": f"Today is {now.strftime("%Y-%m-%d")}"},
        {"role": "user", "content": "Hey"},
    ]
)

vrchat.type_in_chat("Thinking")
vrchat.typing_indicator(True)

# Creates model parameters
completion = openai_client.chat.completions.create(
    model=constant.MODEL_ID,
    messages=history,
    temperature=constant.LM_TEMPERATURE,
    stream=True,
)

# Initialize variables
new_message = {"role": "assistant", "content": ""}
buffer = ""
full_response = ""

for chunk in completion:
    vrchat.typing_indicator(True)
    # Check if the chunk has content
    if chunk.choices[0].delta.content:
        buffer += chunk.choices[0].delta.content
        
        # Process each chunk of text to break it into sentences
        sentence_chunks = word_parse.chunk_text(buffer)
        
        # Process each sentence
        while len(sentence_chunks) > 1:
            # Get the next sentence
            sentence = sentence_chunks.pop(0)
            # Translate the sentence
            sentence = word_parse.translate_text(sentence)
            # Add the sentence to the full response
            full_response += f" {sentence}"
            # Send the sentence to VRChat
            vrchat.type_in_chat(sentence)
            # Create the TTS output
            speech.create_speech_output(sentence)
            # Play the TTS output
            audio.play_tts("output.wav")
            # Parse the sentence for commands
            word_parse.ai_command(sentence)
            
        # Save the remaining text in the buffer
        buffer = sentence_chunks[0]
        
# Process any remaining text after the stream ends
if buffer:
    vrchat.typing_indicator(True)
    # Translate the remaining text
    buffer = translate.translate_text(buffer)
    # Add the remaining text to the full response
    full_response += f" {buffer}"
    # Send the remaining text to VRChat
    vrchat.type_in_chat(buffer)
    # Create the TTS output
    speech.create_speech_output(buffer)
    # Play the TTS output
    audio.play_tts("output.wav")
    # Parse the sentence for commands
    word_parse.ai_command(buffer)
    # Populate the new_message with the remaining text
    new_message["content"] = full_response
    
# Add the full message to the history
history.add(new_message)
# Indicate to the user that the system is done responding
vrchat.typing_indicator(False)

# Get speech input from the user
user_input = ""
while not user_input:
    user_input = speech.get_speech_input()
    
# Load the history from memory
history = history.get()

# Add the user input to the history
history.append({"role": "user", "content": user_input})

# Check for bad words in the user input
bad_words = word_parse.bad_words(user_input)

if bad_words:
    # Combine the bad words into a string
    bad_words_str = ", ".join(bad_words)
    # Report the bad words to the creator
    snapchat.send_message(f"PROFANITY DETECTED: {bad_words_str.upper()} /{user_input}")
    
# Check for commands in the user input
word_parse.user_commands(user_input)