import BombSetup
from Voice import speak


def button(text):
    try:
        color, word = text.split()
    except IndexError:
        speak('Not a button')
        return

    if BombSetup.batts > 1 and word == 'detonate':
        speak("Press the Button")

    elif BombSetup.batts > 2 and BombSetup.frk:
        speak("Press the Button")

    elif color == 'red' and word == 'hold':
        speak("Press the Button")

    else:
        speak("Hold the Button")


def holdbutton(text):
    text = text.lower()

    if 'blue' in text:
        speak('4')
    elif 'yellow' in text:
        speak('5')
    else:
        speak('1')
