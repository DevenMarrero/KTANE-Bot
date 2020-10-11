import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import winsound


def speak(words):
    tts = gTTS(text=words, lang="en")
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    said = ''
    print('getting audio -')
    winsound.Beep(500, 100)
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

