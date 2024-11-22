# NOVA AI

Welcome to NOVA, a dynamic AI assistant for VRChat, designed to interact with users in various moods and respond to voice commands. This README provides an overview of the script, setup instructions, and usage guidelines.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Setup](#setup)
4. [Adding Modes](#adding-modes)
5. [Development](#development)
6. [Contributions](#contributions)
7. [License](#license)

## Overview

NOVA is an AI assistant tailored for VRChat, integrating with OpenAI's API via LM Studio and utilizing Whisper for speech-to-text functionality. The script manages different moods, processes user input, and handles various commands to customize the assistant's behavior.

## Features

- **Voice Commands**: Accepts voice commands to change moods, restart the program, and more.
- **Moods**: Switches between different modes such as normal, argument, drunk, and more.
- **Text-to-Speech**: Converts text responses into speech using `pyttsx3`.
- **Speech Recognition**: Transcribes user speech to text using Whisper.
- **OpenAI Integration**: Utilizes OpenAI’s API with LM Studio for generating responses.

## Setup

### Prerequisites

Ensure you have the following Python libraries installed:

- `openai`
- `pyttsx3`
- `whisper`
- `pydub`
- `pyautogui`
- `keyboard`
- `python-osc`
- `pyaudio`

Install these dependencies using pip:
```sh
pip install openai pyttsx3 pyaudio whisper-openai pydub pyautogui keyboard python-osc
```

### LM Studio Setup

1. Install LM Studio [here](https://lmstudio.ai/).
2. Search for "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF" and download the appropriate model.
3. Navigate to the Local Inference Server page and configure the settings:
    - Tokens to generate: 250
    - CPU threads: 14
    - Enable "Keep entire model in RAM"
4. Click the "Start Server" button.

### Virtual Audio Cables

Install virtual audio cables with at least 2 cables. Example: [Virtual Audio Cable A+B](https://shop.vb-audio.com/en/win-apps/12-vb-cable-ab.html?SubmitCurrency=1&id_currency=1).

Configure VRChat and Windows audio settings:
- VRChat default mic: Cable B
- Windows default input/output: Cable A

### VRChat Configuration

1. Set the input mic to audio cable B.
2. Set the computer's default output to cable A.
3. Enable OSC in VRChat settings.

### Code Setup

1. Install dependencies using the pip command above.
2. Replace placeholders in the code with your system information (e.g., local IP, VRChat port).
3. Set up the audio device index in `audio_device_indexes.py` and update `main.py`.

### Running the Program

1. Start VRChat and LM Studio.
2. Run `main.py` and check the terminal for successful startup messages.

## Adding Modes

1. Create a new system prompt file (e.g., `mad_system_prompt.txt`).
2. Update the `mood_prompts` dictionary in the code.
3. Add new commands in `command_catcher()` and `ai_system_command_catcher()`.
4. Update the `additional_system_prompt.txt` file with the new mode details.

## Development

For development and troubleshooting, refer to the comments and documentation within the code. If you encounter errors, please contact me for help.

## Contributions

[Evan Grinnell](https://github.com/S0L0GUY/NOVA-AI/commits?author=S0L0GUY)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
