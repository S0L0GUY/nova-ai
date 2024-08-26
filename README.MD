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

NOVA is an AI assistant designed for VRChat. It integrates with OpenAI's language model and uses Whisper for speech-to-text functionality. The script manages different moods, processes user input, and handles various commands to customize the assistant's behavior.

## Features

- **Voice Commands**: Accepts voice commands to change moods, restart the program, and more.
- **Moods**: Switches between different modes such as normal, argument, drunk, and more.
- **Text-to-Speech**: Converts text responses into speech using pyttsx3.
- **Speech Recognition**: Transcribes user speech to text using Whisper.
- **OpenAI Integration**: Utilizes OpenAI’s model for generating responses.

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
pip install openai pyttsx3 pyaudio python-osc whisper numpy