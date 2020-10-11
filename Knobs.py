from Voice import speak


def knobs(posask):
    answer = 'not a knob'

    pos = posask.replace(' ', '').replace('three', '3').replace('six', '6').replace('five', '5').replace('two', '2')\
        .replace('to', '2').replace('too', '2').replace('one', '1').replace('-', '')
    if pos == '36' or pos == '35':
        answer = 'UP'

    elif pos == '236' or pos == '0':
        answer = 'Down'

    elif pos == '5':
        answer = 'Left'

    elif pos == '135' or pos == '13':
        answer = 'Right'

    speak(answer)

