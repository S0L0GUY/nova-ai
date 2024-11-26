import commands.vrchat as vrchat
import sys
import os

class program:
    def __init__(self):
        pass
    
    def restart():
        """
        Restarts the current Python program.
        This function sends a message to the VRChat indicating that the program is restarting,
        shows a typing indicator, clears the console, and then restarts the current Python
        program using the same command-line arguments.
        Note:
            This function relies on the 'vrchat' module for sending messages and showing typing
            indicators, and the 'os' and 'sys' modules for restarting the program.
        Raises:
            OSError: If the executable cannot be found or the program cannot be restarted.
        """
        
        vrchat.type_in_chat("Program Restarting...")
        vrchat.typing_indicator(True)
        
        os.system('cls')
        python = sys.executable
        os.execl(python, python, *sys.argv)