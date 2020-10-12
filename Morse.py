from Voice import speak
morse_letters = []


def morse(text):
    global morse_letters
    text = text.replace(' ', '').replace('-', '')
    code = text.replace('one', '-').replace('zero', '.').replace('1', '-').replace('0', '.').replace(':', '')

    morseg = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'r': '.-.',
        's': '...',
        't': '-',
        'v': '...-',
        'x': '-..-',
    }

    codes = {}
    for key, val in morseg.items():
        if code == val:
            morse_letters.append(key)

        codes[val] = key
    try:
        print(str(morse_letters))
    except AssertionError:
        speak('That is not a letter')
        return

    if len(morse_letters) < 2:
        return

    words = {
        'shell 5 0 5',
        'halls 5 1 5',
        'slick 5 2 2',
        'trick 5 3 2',
        'boxes 5 3 5',
        'leaks 5 4 2',
        'strobe 5 4 5',
        'bistro 5 5 2',
        'flick 5 5 5',
        'bombs 5 6 5',
        'break 5 7 2',
        'brick 5 7 5',
        'steak 5 8 2',
        'sting 5 9 2',
        'vector 5 9 5',
        'beats 6 0 0',
    }

    posibles = []
    for word in words:
        for letter in morse_letters:
            if letter in word:
                if word not in posibles:
                    posibles.append(word)
            else:
                if word in posibles:
                    posibles.remove(word)
                break
    if len(posibles) == 1:
        janswer = ' '.join([str(elem) for elem in posibles])
        speak(janswer)
    else:
        speak('Not enough letters')
        return


def resetmorse():
    global morse_letters
    morse_letters = []

