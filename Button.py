import BombSetup
from Voice import speak

colours = ['blue', 'red', 'white', 'yellow', 'black']
words = ['abort', 'detonate', 'hold', 'press']


def button(text):
    colour = ''
    word = ''
    for w in words:
        if w in text:
            word = w

    for c in colours:
        if c in text:
            colour = c

    if '' == (colour or word):
        speak('Not a button')
        return

    if BombSetup.batts > 1 and word == 'detonate':
        speak("Press the Button")

    elif BombSetup.batts > 2 and BombSetup.frk:
        speak("Press the Button")

    elif colour == 'red' and word == 'hold':
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
