import pygame
import time
import os

# Initialize Pygame and Joystick
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick detected.")
    exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Controller name: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

def clear_screen():
    """Check the operating system and clear the termanal."""    
    os.system('cls' if os.name == 'nt' else 'clear')

# Main loop to capture all controller values

def get_joystick_inputs():
    """
    Returns:
        string: All of the values of the controller.

    Display all of the values of an x-box controller.
    """    
    output = ""
    pygame.event.pump()  # Updates pygame events

    # Get and print all axis values (analog sticks, triggers)
    for i in range(joystick.get_numaxes()):
        axis_value = joystick.get_axis(i)
        output = f"{output}\n{axis_value}"

    # Get and print all button values (A, B, X, Y, etc.)
    for i in range(joystick.get_numbuttons()):
        button_value = joystick.get_button(i)
        output = f"{output}\n{button_value}"

    # Get and print all hat (D-pad) values
    for i in range(joystick.get_numhats()):
        hat_value = joystick.get_hat(i)
        output = f"{output}\n{hat_value}"

    return output

while True:
    print(get_joystick_inputs())
    clear_screen()

# Quit Pygame
pygame.quit()