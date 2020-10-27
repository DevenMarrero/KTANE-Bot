import speech_recognition as sr
import winsound
import pyttsx3


def speak(words):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)

    engine.say(words)
    engine.runAndWait()


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

