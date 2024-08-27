# NOVA VRChat AI Assistant

Welcome to NOVA, a versatile VRChat AI assistant designed to interact with users in various moods and respond to voice commands. This README provides an overview of the script, its setup, and usage instructions.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Development](#development)
6. [License](#license)

## Overview

NOVA is an AI assistant designed for VRChat. It integrates with OpenAI's API with LM Studio and uses Whisper for speech-to-text functionality. The script manages different moods, processes user input, and handles various commands to customize the assistant's behavior.

## Features

- **Voice Commands**: Accepts voice commands to change moods, restart the program, and more.
- **Moods**: Switches between different modes such as normal, argument, drunk, and more.
- **Text-to-Speech**: Converts text responses into speech using pyttsx3.
- **Speech Recognition**: Transcribes user speech to text using Whisper.
- **OpenAI Integration**: Utilizes OpenAI’s API with LM Studio for generating responses.

## Setup

For reference, my computer hardware:
- Intel Core 17-4790
- NVIDIA GeForce GTX 1050Ti
- 16 GB DDR3 RAM

This means that the AI should really be able to run on anything that can have VR Chat and VS Code open at the same time, it will just mean that ~NOVA~ will run a little bit slower.

### Prerequisites

Ensure you have the following Python libraries installed:

- `openai`
- `pyttsx3`
- `pyaudio`
- `pythonosc`
- `whisper`
- `numpy`
- `re`

You can install these dependencies using pip:

```sh
pip install openai pyttsx3 pyaudio python-osc whisper numpy pydub
```

Install LM studio [HERE](https://lmstudio.ai/). Once LM Studios is installed and set up, Navigate to the magnifying glass button and search for "
lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF" and download whichever model runs on your system best. I personally use the "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf" model but you can get faster with some of the other models. After that, look on the left side of the screen for a logo that is just 2 arrows connected together pointing opposite directions, and click on it. This should bring you to the Local Inference Server page. It gets a little tricky here because these settings may verry from system to system. To get ~NOVA~ to respond so fast on my system, I have the tokens to generate set to 250, and the CPU threads set to 14. I also set "Keep entire model in RAM" to on because why not. If you don't see any of these options they may be in dropdown menus or something. Now whenever you are ready to run ~NOVA~ your first step is to open this app, navigate to this page, and click the big green "Start Server" button.

Install any virtual audio cables, as long as there are 2 cables it will work. I used [Vertual Audio Cable A+B](https://shop.vb-audio.com/en/win-apps/12-vb-cable-ab.html?SubmitCurrency=1&id_currency=1) But this option is donationwhere so you have to pay for it. Any generic virtual audio cables will work as long as there are 2. I am going to call them cables A and B just for clarity's sake. As it says at the top of main.py, in VR Chat set your default mic to cable B, and in the audio control panel on Windows, set both your default input and output cables to cable A. This does make it so you cannot hear what ~NOVA~ is hearing or saying, so if you find a workaround then go for it.

VR Chat can just run in the background, nothing special with it. You will need to set the input mic to audio cable B and set your computer's default output to cable A. I would suggest setting your AI's account to have an earmuff bubble. Set the outside sound level to 0. I set the cone to the max that I could but the actual bubble is at 35%. Also, enable OSC. Look for a tutorial on YouTube if you don't know how to do it.

For the actual code portion of this setup, it is really straight forward. As showen above, using your terminal, type in the pip statement with all of the dependencies listed. Take a look through all of the code and prompts to see how she works. That step is helpful because you will be able to better diagnose problems in the future. It also explains a little why she acts the way she does. You will find some comments saying things like "Your computers local IP" or "VR Chat port". Replace these with your system information. The IP needs to be your local IP so it will be the one that starts with 192.168.0.--. VR Chats port should stay the same. At this point, it would be a good time to set up the audio device index. In the "audio device indexes.py" file, run the script and look in the terminal. Your going to want to look for the first instance of "CABLE-B Input (VB-Audio Cable B" or whatever your B cable is called. Back in main.py, record the index of your audio device to the audio_device_index variable (replace 6 with your number).

When you are ready to run the program, have VR Chat and LM Studio running and booted to the correct places. Open the main.py file and run it. If the terminal looks like this after a minute then you know that your program worked.

07:14:19 2024-08-27 SYSTEM: Program started

07:14:19 2024-08-27 IMPORT: Debug imported

07:14:22 2024-08-27 IMPORT: Successfully imported openai, pyttsx3, os, time, pyaudio, pythonosc, re, wave, sys, whisper, numpy, pydub

07:14:38 2024-08-27 AI: Hi!

07:14:39 2024-08-27 AI: I'm Nova.

07:14:41 2024-08-27 AI: Nice to meet you in VR Chat.

07:14:43 2024-08-27 AI: What brings you here today?

If it does not look like this, and there is an error, paste the error into chat GPT and ask it for help.

## Adding Modes

Adding modes is easy, you are going to want to first create the prompt (I usually ask chat GPT to do it). You dont want the prompt to mention things like her name or that she has other modes because that is explained in the additional system prompt. Create a new file called "(mood)_system_prompt.txt" so if you wher making a mad mood, you would want to name it "mad_system_prompt.txt". Paste the system prompt into the file. Now locate the variadable called "mood_prompts" and fallow the format of the other entrys. Add the comma at the end of the last entry and create a new entry. In my example it would look like ""mad": 'text_files/prompts/mad_system_prompt.txt'". Now your going to want to add the command so that a player can put her in the mood. In "main.py" locate the function called "command_catcher()". You will want to scroll to the bottom of the function and add a new elif statement. I will usually just copy an ole elif statement and replace it with the new data. For example this is how i would fill out my new mode:

elif "activate mad mode" in user_input.lower():
        debug_write("COMMAND CATCHER", "Mad Mode Called")
        with open('var/mood.txt', 'w') as file:
            file.write('mad')
        restart_program()

It is really streight forward. You are also going to want to do this for "ai_system_command_catcher()". This function parces what the ai says for commands so you will want it to say "activate my mad mode now" insted of "activate mad mode".
