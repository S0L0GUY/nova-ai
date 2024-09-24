import pyttsx3

'''
List all of the voices avalable for pyttsx3 on this system.
'''

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print(f"ID: {voice.id}\nName: {voice.name}\nGender: {voice.gender}\nLanguage: {voice.languages}\n")