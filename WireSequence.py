from Voice import speak

counts = []
redc = 0
bluec = 0
blackc = 0

sequences = {'red': [
    ('c'),
    ('b'),
    ('a'),
    ('a', 'c'),
    ('b'),
    ('a', 'c'),
    ('a', 'b', 'c'),
    ('a', 'b'),
    ('b')
], 'blue': [
    ('b'),
    ('a', 'c'),
    ('b'),
    ('a'),
    ('b'),
    ('b', 'c'),
    ('c'),
    ('a', 'c'),
    ('a')
], 'black': [
    ('a', 'b', 'c'),
    ('a', 'c'),
    ('b'),
    ('a', 'c'),
    ('b'),
    ('b', 'c'),
    ('a', 'b'),
    ('c'),
    ('c')
]}


def sequence(text):
    global sequences
    global redc
    global bluec
    global blackc
    wireask = text.lower()

    if 'stop' not in wireask:
        wireask = wireask.replace('alpha', 'a').replace('bravo', 'b').replace('charlie', 'c').replace('read', 'red')
        wires = wireask.split(' next ')
        answer = []

        for index, item in enumerate(wires):
            item = item.split(' ')

            try:
                color, letter = item
            except ValueError:
                speak('Say Next in Between Wires')
                return

            if letter in sequences[str('red')][redc] and color == 'red':
                answer.append('Yes,')

            elif letter in sequences[str('blue')][bluec] and color == 'blue':
                answer.append('Yes,')

            elif letter in sequences[str('black')][blackc] and color == 'black':
                answer.append('Yes,')
            else:
                answer.append("No,")

            if color == 'red':
                redc += 1

            elif color == 'blue':
                bluec += 1

            else:
                blackc += 1

        janswer = ' '.join([str(elem) for elem in answer])
        speak(janswer)


def resetsequence():
    global redc, blackc, bluec
    redc, blackc, bluec = 0, 0, 0
