from Voice import speak

vowel = True
even = False
batts = 0
parallelport = False
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


def serial(text):
    global vowel
    global even
    text = text.replace('foul', 'vowel').replace('bowel', 'vowel').replace('dowel', 'vowel').replace('rod', 'odd')
    if 'vowel' in text:
        vowel = True

    if 'even' in text:
        even = True


def port():
    global parallelport
    parallelport = True


def indicators(text):
    global frk
    global car
    if 'freak' in text:
        frk = True
    if 'car' in text:
        car = True


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
    global even
    global batts
    global parallelport
    global frk
    global car
    global strikes
    vowel = False
    even = False
    batts = 0
    parallelport = False
    frk = False
    car = False
    strikes = 0
