from Voice import speak

answer = []


def keypad(text):
    symbols = text.lower()

    groups = [
        ['balloon', 'alpha', 'alfa', 'lambda', 'lightning', 'kitty', 'h', 'hotel', 'charlie'],
        ['euro', 'balloon', 'charlie', 'cursive', 'star', 'h', 'hotel', 'question'],
        ['copyright', 'nose', 'knows', 'cursive', 'butterfly', ';', 'lambda', 'star'],
        ['six', '6', 'paragraph', 'b', 'bravo', 'kitty', 'butterfly', 'question', 'smile', 'smiley'],
        ['trident', 'smile', 'smiley', 'b', 'bravo', 'c', 'charlie', 'paragraph', 'three', '3', 'star'],
        ['six', '6', 'euro', 'puzzle', 'smash', 'trident', 'november', 'omega']
    ]

    curr_symbols = symbols.replace('.', '').replace(';', ' ;').split()

    for group in groups:
        for symbol in curr_symbols:
            if symbol not in group:
                break
        else:
            for symbol in group:
                if symbol in curr_symbols:
                    answer.append(symbol)

    janswer = ' '.join([str(elem) for elem in answer])
    janswer = janswer.replace(';', 'semicolon')
    try:
        speak(janswer)
    except AssertionError:
        speak('A symbol does not exist')
        return 

    return
