from pythonosc import udp_client
import time
import os
import random


local_ip = "192.168.0.19" # Your computers local IP
port = 9000 # VR Chat port, 9000 is the default
osc_client = udp_client.SimpleUDPClient(local_ip, port)

while True:
    random_number = random.randint(1, 3)
    if random_number == 1:
        random_number = random.randint(1, 3)
        osc_client.send_message("/input/MoveForward", 1)
        time.sleep(random_number)
        osc_client.send_message("/input/MoveForward", 0)
    elif random_number == 2:
        osc_client.send_message("/input/LookLeft", 1)
        time.sleep(0.4)
        osc_client.send_message("/input/LookLeft", 0)
    elif random_number == 3:
        osc_client.send_message("/input/LookRight", 1)
        time.sleep(0.4)
        osc_client.send_message("/input/LookRight", 0)