from commands.system_prompts import prompt
from commands.vrchat import vrchat
from openai import OpenAI
import pyautogui
import datetime
import keyboard

class snapchat:
    def __init__(self):
        openai_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        
        snapchat_system_prompt = prompt.get_system_prompt("snapchat")
        
        snapchat_history=[
            {"role": "system", "content": snapchat_system_prompt},
        ]
    
    def send_message(self, message, ai_generated=False):
        """
        Sends a message on Snapchat, optionally generating a response using AI.
        Args:
            message (str): The message to be sent.
            ai_generated (bool, optional): If True, the message will be processed and responded to by an AI. Defaults to False.
        Returns:
            None
        """
        
        # Type to the VR Chat textbox saying that the message was flagged
        flagged_message = "🚩MESSAGE FLAGGED🚩\nSending message to creator..."
        vrchat.type_in_chat(flagged_message)
        vrchat.typing_indicator(True)
        
        # Get the current date and time
        now = datetime.now()
        date = now.strftime("%m/%d/%Y %I:%M %p")

        if ai_generated:
            # Append the message to Snapchat
            self.snapchat_history.append({"role": "user", "content": message})

            # Type the heder
            pyautogui.typewrite(f"~~~~{date}~~~~")
            pyautogui.press("enter")

            new_message = {"role": "assistant", "content": ""}

            # Create a response with AI
            completion = self.openai_client.chat.completions.create(
                model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
                messages=self.snapchat_history,
                temperature=0.2,
                stream=True,
            )
        
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    new_message["content"] += chunk.choices[0].delta.content

            pyautogui.typewrite(new_message["content"])
            self.snapchat_history.append(new_message)
        else:
            # Type the heder
            pyautogui.typewrite(f"~~~~{date}~~~~")
            pyautogui.press("enter")
            
            pyautogui.typewrite(message)

        keyboard.press_and_release("enter")
