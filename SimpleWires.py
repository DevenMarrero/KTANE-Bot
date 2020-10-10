import Setup
from Voice import speak


def simplewires(text):
    colors = text.replace('read', 'red')
    scolors = (colors.split(' '))
    wires = str(len(scolors))

    if wires == '3':
        w3 = scolors[2]

        if colors.count('red') == 0:
            speak("Second Wire")

        elif w3 == 'white':

            speak("Last Wire")

        elif colors.count('u') > 1:
            speak("Last Blue Wire")

        else:
            speak("Last Wire")

    if wires == '4':
        w4 = scolors[3]

        if colors.count('red') > 1 and Setup.even_odd == 'odd':
            speak('last red wire')

        elif w4 == 'yellow' and colors.count('red') == 0:
            speak("Cut First Wire")

        elif colors.count('blue') == 1:
            speak('First Wire')

        elif colors.count('yellow') > 1:
            speak('Last Wire')

        else:
            speak('Second Wire')

    if wires == '5':
        w5 = scolors[4]

        if w5 == 'black' and Setup.even_odd == 'odd':
            speak('Fourth Wire')

        elif colors.count('red') == 1 and colors.count('yellow') > 1:
            speak('First Wire')

        elif colors.count('black') == 0:
            speak('Second Wire')

        else:
            speak('First Wire')

    if wires == '6':

        if colors.count('yellow') == 0 and Setup.even_odd == 'odd':
            speak('Third wire')

        elif colors.count('yellow') == 1 and colors.count('white') > 1:
            speak('Fourth Wire')

        elif colors.count('red') == 0:
            speak('Last Wire')

        else:
            speak('Fourth Wire')