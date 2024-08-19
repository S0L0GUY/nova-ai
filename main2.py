'''
import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Device {i}: {info['name']}")
'''
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print(f"ID: {voice.id}\nName: {voice.name}\nGender: {voice.gender}\nLanguage: {voice.languages}\n")
