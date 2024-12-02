import constants as constant
import socket

class VRChatOSC:
    def __init__(self, ip=constant.IP, port=constant.PORT):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message):
        """
        Sends a message to the specified IP and port using the OSC protocol.
        Args:
            message (str): The message to be sent.
        """

        osc_message = f"/chatbox/input {message}\0"
        self.sock.sendto(osc_message.encode('utf-8'), (self.ip, self.port))

    def set_typing_indicator(self, is_typing):
        """
        Sends a typing indicator message to the specified OSC (Open Sound Control) endpoint.
        Args:
            is_typing (bool): A boolean indicating whether the typing indicator should be on (True) or off (False).
        Sends:
            A message in the format "/chatbox/typing {0 or 1}\0" to the OSC endpoint defined by self.ip and self.port.
        """

        osc_message = f"/chatbox/typing {int(is_typing)}\0"
        self.sock.sendto(osc_message.encode('utf-8'), (self.ip, self.port))