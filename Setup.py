from Voice import speak, get_audio

vowel = ''
global even_odd
batts = 0
global parallelport
frk = False
car = False
strikes = 0


def setup():
    global vowel
    global even_odd
    global batts
    global parallelport
    global frk
    global car
    global strikes

    speak('Serial Number')
    text = get_audio()
    text.replace('foul', 'vowel').replace('bowel', 'vowel').replace('dowel', 'vowel').replace('rod', 'odd')

    if 'vowel yes' in text:
        vowel = 'yes'
    else:
        vowel = 'no'
    print(vowel)

    if 'even' in text:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(even_odd)

    speak('Batteries, Port, Freak, and Car')
    txt = get_audio()
    text = txt.replace('two', '2').replace('to', '2').replace('too', '2').replace('freaky', 'freak')\
        .replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('zero', '0')\
        .replace('for', '4').replace('one', '1')
    batts = int(text[0])
    print(batts)

    if 'port yes' in text:
        parallelport = 'yes'
    else:
        parallelport = 'no'

    if 'freak yes' in text:
        frk = True
    else:
        frk = False

    if 'car yes' in text:
        car = True
    else:
        car = False

    speak('Setup Complete')


def addstrike():
    global strikes
    strikes += 1
    speak(f'Strike Added, {strikes} total')


def removestrike():
    global strikes
    strikes -= 1
    speak(f'Strike Removed, {strikes} total')
