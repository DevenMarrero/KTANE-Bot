from Voice import speak

vowel = 'no'
even_odd = 'odd'
batts = 0
parallelport = 'no'
frk = False
car = False
strikes = 0


def batteries(text):
    global batts
    text = text.replace('zero', '0').replace('one', '1').replace('two', '2').replace('to', '2').replace('too', '2') \
        .replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('for', '4')
    try:
        batts = int(text)
    except ValueError:
        speak("Try batteries again")
    print(batts)


def serial(text):
    global vowel
    global even_odd
    text = text.replace('foul', 'vowel').replace('bowel', 'vowel').replace('dowel', 'vowel').replace('rod', 'odd')
    if 'vowel' in text:
        vowel = 'yes'

    if 'even' in text:
        even_odd = 'even'
    print(vowel, even_odd)


def port():
    global parallelport
    parallelport = 'yes'


def indicators(text):
    global frk
    global car
    if 'freak' in text:
        frk = True
    if 'car' in text:
        car = True
    print(frk, car)


def addstrike():
    global strikes
    strikes += 1
    speak(f'Strike Added, {strikes} total')


def removestrike():
    global strikes
    strikes -= 1
    speak(f'Strike Removed, {strikes} total')


def resetsetup():
    global vowel
    global even_odd
    global batts
    global parallelport
    global frk
    global car
    global strikes
    vowel = 'no'
    even_odd = 'odd'
    batts = 0
    parallelport = 'no'
    frk = False
    car = False
    strikes = 0
