from pythonosc import udp_client

class NovaOSCLibrary:
    def __init__(self, ip='127.0.0.1', port=9000):
        self.client = udp_client.SimpleUDPClient(ip, port)

    def look_at(self, x, y, z):
        """
        Send the coordinates (x, y, z) where NOVA should look.
        """
        self.client.send_message("/nova/look_at", [x, y, z])

    def reset_view(self):
        """
        Reset NOVA's view to a default position.
        """
        self.client.send_message("/nova/reset_view", [])