import BombSetup
from Voice import speak
answer = []


def compwires(text):

    wires = text.split(' next ')

    for wire in wires.lower():

        if 'red' in wire:
            red = True
        else:
            red = False

        if 'blue' in wire:
            blue = True
        else:
            blue = False

        if 'star' in wire:
            star = True
        else:
            star = False

        if 'led' in wire:
            led = True
        else:
            led = False

        # Just Cut
        if red and not blue and star and not led:
            answer.append('Yes, ')

        elif not red and not blue and star and not led:
            answer.append('Yes, ')

        elif not red and not blue and not star and not led:
            answer.append('Yes, ')

        # Cut if Serial is Even
        elif (red and blue and not star and led) and BombSetup.even:
            answer.append('Yes, ')

        elif (red and blue and not star and not led) and BombSetup.even:
            answer.append('Yes, ')

        elif (red and not blue and not star and not led) and BombSetup.even:
            answer.append('Yes, ')

        elif (not red and blue and not star and not led) and BombSetup.even:
            answer.append('Yes, ')

        # Cut if Parallel Port
        elif (red and blue and star and not led) and BombSetup.parallelport:
            answer.append('Yes, ')

        elif (not red and blue and star and led) and BombSetup.parallelport:
            answer.append('Yes, ')

        elif (not red and blue and not star and led) and BombSetup.parallelport:
            answer.append('Yes, ')

        # Cut if Bomb has 2 or More Batteries
        elif (red and not blue and star and led) and (BombSetup.batts > 1):
            answer.append('Yes, ')

        elif (red and not blue and not star and led) and (BombSetup.batts > 1):
            answer.append('Yes, ')

        elif (not red and not blue and star and led) and (BombSetup.batts > 1):
            answer.append('Yes, ')

        else:
            answer.append("No")

    janswer = ' '.join([str(elem) for elem in answer])
    speak(janswer)
