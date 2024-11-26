import commands.snapchat as snapchat
import commands.program as program
import commands.vrchat as vrchat
import commands.mood as mood
import time
import json
import re

class parse:
    def __init__(self):
        with open('variable/bad_words.json', 'r') as file:
            bad_words = json.load(file)
    
    def bad_words(self, string_to_check):
        """
        Checks a given string for the presence of any bad words.
        Args:
            string_to_check (str): The string to be checked for bad words.
        Returns:
            list: A list of bad words found in the given string.
        """
        
        return [word for word in self.bad_words if word in string_to_check]

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
    
    def user_commands(user_input):
        """
        Processes user commands and sets the appropriate mode or action based on the input.
        Args:
            user_input (str): The input command from the user.
        """
        
        if "system reset" in user_input.lower():
            snapchat.send_message("SYSTEM RESET CALLED BY PLAYER")
            program.restart()
        elif "activate argument mode" in user_input.lower():
            mood.set("argument")
            snapchat.send_message("ARGUMENT MODE CALLED BY PLAYER")
            program.restart()
        elif "activate normal mode" in user_input.lower():
            mood.set("normal")
            snapchat.send_message("NORMAL MODE CALLED BY PLAYER")
            program.restart()
        elif "stop talking" in user_input.lower() or "shut up" in user_input.lower() or "time out" in user_input.lower():
            snapchat.send_message("STOP TALKING CALLED BY PLAYER")
            time_left = 60
            while time_left > 0:
                vrchat.type_in_chat(f"Timeout Period: {str(time_left)}")
                time_left -= 2
                time.sleep(2)
            program.restart()
        elif "activate misinformation mode" in user_input.lower():
            mood.set("misinformation")
            snapchat.send_message("MISINFORMATION MODE CALLED BY PLAYER")
            program.restart()
        elif "get drunk" in user_input.lower():
            mood.set("drunk")
            snapchat.send_message("DRUNK MODE CALLED BY PLAYER")
            program.restart()
        elif "activate depressed mode" in user_input.lower():
            mood.set("depressed")
            snapchat.send_message("DEPRESSED MODE CALLED BY PLAYER")
            program.restart()
        elif "activate therapy mode" in user_input.lower():
            mood.set("therapy")
            snapchat.send_message("THERAPY MODE CALLED BY PLAYER")
            program.restart()
        elif "activate anxious mode" in user_input.lower():
            mood.set("anxious")
            snapchat.send_message("ANXIOUS MODE CALLED BY PLAYER")
            program.restart()
        elif "activate sarcasm mode" in user_input.lower():
            mood.set("sarcasm")
            snapchat.send_message("SARCASM MODE CALLED BY PLAYER")
            program.restart()
        elif "activate pleasing mode" in user_input.lower():
            mood.set("pleasing")
            snapchat.send_message("PLEASING MODE CALLED BY PLAYER")
            program.restart()

    def ai_command(ai_input):
        """
        Processes user commands and sets the appropriate mode or action based on the input.
        Args:
            ai_input (str): The input command from the AI.
        """

        if "reset my system now" in ai_input.lower():
            snapchat.send_message("SYSTEM RESET CALLED BY ~NOVA~")
            program.restart()
        elif "enter angry mode now" in ai_input.lower():
            mood.set("argument")
            snapchat.send_message("ANGRY MODE CALLED BY ~NOVA~")
            program.restart()
        elif "activate normal mode now" in ai_input.lower():
            mood.set("normal")
            snapchat.send_message("NORMAL MODE CALLED BY ~NOVA~")
            program.restart()
        elif "stop talking now" in ai_input.lower():
            snapchat.send_message("TIMEOUT CALLED BY ~NOVA~")
            time_left = 60
            while time_left > 0:
                vrchat.type_in_chat(f"Timeout Period: {str(time_left)}")
                time_left -= 2
                time.sleep(2)
            program.restart()
        elif "activate wrong information now" in ai_input.lower():
            mood.set("misinformation")
            snapchat.send_message("MISINFORMATION MODE CALLED BY ~NOVA~")
            program.restart()
        elif "activate drunk mode now" in ai_input.lower():
            mood.set("drunk")
            snapchat.send_message("DRUNK MODE CALLED BY ~NOVA~")
            program.restart()
        elif "activate my depressed mode now" in ai_input.lower():
            mood.set("depressed")
            snapchat.send_message("DEPRESSED MODE CALLED BY ~NOVA~")
            program.restart()
        elif "activate my therapy mode now" in ai_input.lower():
            mood.set("therapy")
            snapchat.send_message("THERAPY MODE CALLED BY ~NOVA~")
            program.restart()
        elif "activate my anxious mode now" in ai_input.lower():
            mood.set("anxious")
            snapchat.send_message("ANXIOUS MODE CALLED BY ~NOVA~")
            program.restart()
        elif "activate my sarcasm mode now" in ai_input.lower():
            mood.set("sarcasm")
            snapchat.send_message("SARCASM MODE CALLED BY ~NOVA~")
            program.restart()
        elif "activate my pleasing mode now" in ai_input.lower():
            mood.set("pleasing")
            snapchat.send_message("PLEASING MODE CALLED BY ~NOVA~")
            program.restart()
