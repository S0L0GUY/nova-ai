import variable.constants as constant
from pythonosc import udp_client

class vrchat():
    def __init__(self):
        # Set up OSC for chat and movement
        self.osc_client = udp_client.SimpleUDPClient(constant.LOCAL_IP, constant.VRC_PORT)

    def type_in_chat(self, message):
        """
        Args:
            message (string): The message that you want to type in chat.

        Type a message into Nova's VR Chat game using OSC
        """
        self.osc_client.send_message("/chatbox/input", [message, True])

    def typing_indicator(self, switch):
        self.osc_client.send_message("/chatbox/typing", switch)