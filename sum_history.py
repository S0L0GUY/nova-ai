from openai import OpenAI
import json
from datetime import datetime
import pyautogui
import keyboard

openai_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

with open('history.json', 'r') as file:
    old_history = json.load(file)

def send_message_snapchat(message):
    now = datetime.now()
    date = now.strftime("%m/%d/%Y %I:%M %p")

    pyautogui.typewrite(f'~~~~{date}~~~~')
    pyautogui.press('enter')

    pyautogui.typewrite(message)

    keyboard.press_and_release('enter')

history = [
    {"role": "system", "content": "Create a short, 4 sentence or less summery for all that is said in this conversation?"},
    {"role": "user", "content": json.dumps(old_history, indent=4)},
]

completion = openai_client.chat.completions.create(
    model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
    messages=history,
    temperature=0.2,
    stream=True,
)

new_message = {"role": "assistant", "content": ""}

for chunk in completion:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
        new_message["content"] += chunk.choices[0].delta.content

send_message_snapchat(f"CONVERSATION SUMMERY: {new_message['content']}")