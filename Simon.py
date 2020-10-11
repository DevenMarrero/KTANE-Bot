import BombSetup
from Voice import speak


def simon(text):
    flash = text.replace('blue', 'b').replace('red', 'r').replace('yellow', 'y').replace('green', 'g')

    if BombSetup.vowel == 'yes':

        if BombSetup.strikes == 0:
            flash = flash.replace('r', "BLUE, ")
            flash = flash.replace('b', "RED, ")
            flash = flash.replace('g', "YELLOW, ")
            flash = flash.replace('y', "GREEN, ")

        elif BombSetup.strikes == 1:
            flash = flash.replace('r', "YELLOW, ")
            flash = flash.replace('b', "GREEN, ")
            flash = flash.replace('g', "BLUE, ")
            flash = flash.replace('y', "RED, ")

        else:
            flash = flash.replace('r', "GREEN, ")
            flash = flash.replace('b', "RED, ")
            flash = flash.replace('g', "YELLOW, ")
            flash = flash.replace('y', "BLUE, ")

    else:
        if BombSetup.strikes == 0:
            flash = flash.replace('r', "BLUE...")
            flash = flash.replace('b', "YELLOW...")
            flash = flash.replace('g', "GREEN...")
            flash = flash.replace('y', "RED...")

        elif BombSetup.strikes == 1:
            flash = flash.replace('r', "RED, ")
            flash = flash.replace('b', "BLUE, ")
            flash = flash.replace('g', "YELLOW, ")
            flash = flash.replace('y', "GREEN, ")

        else:
            flash = flash.replace('r', "YELLOW, ")
            flash = flash.replace('b', "GREEN, ")
            flash = flash.replace('g', "BLUE, ")
            flash = flash.replace('y', "RED ")
    speak(flash)
