from Voice import speak


def password(text):
    curr_password = []
    crow1 = []
    crow3 = []

    txt = text.lower()
    text = txt.split(' next ')
    try:
        row1 = text[0].split()
        row3 = text[1].split()
    except IndexError:
        speak('Say Next in between rows')
        return 

    for word in row1:
        lrow = word.replace(word, word[0])
        crow1.append(lrow)

    letters = ' '.join([str(elem) for elem in crow1])
    curr_password.append(letters)

    for word in row3:
        lrow = word.replace(word, word[0])
        crow3.append(lrow)

    letters = ' '.join([str(elem) for elem in crow3])
    curr_password.append(letters)

    print(curr_password)

    passwords = ['about',
                 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great',
                 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point',
                 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there',
                 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world',
                 'would', 'write']

    posibles = []
    for password in passwords:
        if password[0] in curr_password[0] and password[2] in curr_password[1]:
            posibles.append(password)

    janswer = ' '.join([str(elem) for elem in posibles])
    speak(janswer)
    curr_password = []

