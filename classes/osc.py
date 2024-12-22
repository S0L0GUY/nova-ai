from pythonosc import udp_client

class VRChatOSC:
    def __init__(self, ip: str, port: int):
        self.client = udp_client.SimpleUDPClient(ip, port)

    def send_message(self, message: str):
        self.client.send_message("/chatbox/input", [message, True])
        self.client.send_message("/chatbox/typing", False)

    def set_typing_indicator(self, typing: bool):
        self.client.send_message("/chatbox/typing", typing)