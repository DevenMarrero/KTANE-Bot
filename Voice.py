import os
import playsound
import speech_recognition as sr
from gtts import gTTS
said = ''


def speak(words):
    tts = gTTS(text=words, lang="en")
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    global said
    print('getting audio -')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.dynamic_energy_threshold = False
        r.energy_threshold = 150
        audio = r.listen(source)

        try:
            said = r.recognize_google(audio)
            if said == "":
                get_audio()
            print(said)
        except Exception:
            print("Exception")
            get_audio()

    return said

