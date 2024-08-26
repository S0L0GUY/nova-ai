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
lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF" and download whichever model runs on your system best. I personally use the "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf" model but you can get faster with some of the other models.

Install any virtual audio cables, as long as there are 2 cables it will work. I used [Vertual Audio Cable A+B](https://shop.vb-audio.com/en/win-apps/12-vb-cable-ab.html?SubmitCurrency=1&id_currency=1) But this option is donationwhere so you have to pay for it.

VR Chat can just run in the background, nothing special with it. You will need to set the input mic to audio cable B and set your computer's default output to cable A.
