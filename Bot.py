from Voice import speak, get_audio

import Knobs
import CompWires
import OnFirst
import WireSequence
import Memory
import Maze
import Button
import BombSetup
import Password
import Morse
import KeyPad
import SimpleWires
import Simon

import multiprocessing


def total_reset():
    Morse.resetmorse()
    WireSequence.resetsequence()
    Morse.resetmorse()
    BombSetup.resetsetup()
    speak('Bomb Reset')


if __name__ == '__main__':
    multiprocessing.freeze_support()

    while True:
        txt = get_audio().lower()
        text = txt.replace("moore's", 'morse').replace("/", ' ')

        # Modules
        if 'simple wires' in text:  # Name all wires. ie(red, blue, red)
            text = text.replace('.', '').replace('wires ', '')
            SimpleWires.simplewires(text)

        elif 'button' in text:  # Colour then word ie(yellow Press)
            text = text.replace('button ', '')
            Button.button(text)

        elif 'strip' in text:  # Color ie(Red)
            text = text.replace('strip ', '')
            Button.holdbutton(text)

        elif 'keypad' in text:  # Say symbols
            text = text.replace('keypad ', '').replace('symbols ', '')
            KeyPad.keypad(text)

        elif 'simon' in text:  # Say colours ie(Red, Red, Blue)
            text = text.replace('simon ', '')
            Simon.simon(text)

        elif "words" in text or "on 1st" in text:  # Word on screen, then word on told button
            text = text.replace("words ", '').replace("on 1st ", '')
            if OnFirst.onfirst(text):
                answer = OnFirst.onfirstwords()
                p = multiprocessing.Process(target=speak, args=(answer,))
                p.start()

                while p.is_alive():
                    listen = get_audio()
                    if listen == 'stop':
                        p.terminate()

        elif 'reset memory' in text:
            Memory.resetmemstage()
            speak('Memory reset')

        elif 'memory' in text:  # Number on screen
            text = text.replace('for ', '4').replace('memory ', '')
            Memory.memory(text)

        elif 'reset morse' in text:
            Morse.resetmorse()
            speak('Morse reset')

        elif 'morse' in text:  # Sets of flashes ie(dot dot dash) or (0 0 1)
            text = text.replace('morse ', '')
            Morse.morse(text)

        elif 'complicated' in text:  # Wire attributes separated by 'next' ie(red star next blue)
            text = text.replace('complicated ', '').replace('read', 'red')
            CompWires.compwires(text)

        elif 'sequence' in text or 'sequins' in text:  # colour then letter sep by 'next' ie(red alpha next blue bravo)
            text = text.replace('sequins ', '').replace('sequence ', '')
            WireSequence.sequence(text)

        elif 'reset sequence' in text:
            WireSequence.resetsequence()
            speak('Sequence Reset')

        elif 'maze' in text or 'maize' in text or "may's" in text:  # 1 Indicator, start, finish sep by 'next' ie(44 next 43 next 55)
            text = text.replace('maze ', '').replace('maize ', '').replace("may's ", '')
            Maze.maze(text)

        elif 'password' in text:  # Nato alphabet for each letter sep by 'next' ie(lima next alpha)
            text = text.replace('password ', '').replace('hilo', 'kilo')
            Password.password(text)

        elif 'knobs' in text:  # column of LEDs with top and bottom lit ie(135)
            text = text.replace('knobs ', '')
            Knobs.knobs(text)

        # Setup
        elif 'batteries' in text:
            text = text.replace('batteries ', '')
            BombSetup.batteries(text)

        elif 'serial' in text or 'cereal' in text:
            text = text.replace('serial ', '')
            BombSetup.serial(text)

        elif 'parallel port' in text:
            text = text.replace('port ', '').replace('parallel port ', '')
            BombSetup.port()

        elif 'indicators' in text:
            text = text.replace('indicators ', '')
            BombSetup.indicators(text)

        # Commands
        elif 'add strike' in text:
            BombSetup.addstrike()

        elif 'remove strike' in text:
            BombSetup.removestrike()

        elif text == 'the bomb is complete':
            speak('We did it')
            total_reset()

        elif 'we blew up' in text:
            speak("It's Not my Fault, i'm the bot")
            total_reset()

        elif 'bomb reset' in text:
            total_reset()

        elif 'exit program' in text:
            speak('Goodbye')
            break
