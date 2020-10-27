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
            text = text.replace('.', '').replace('simple wires ', '')
            SimpleWires.simplewires(text)

        elif 'button' in text or 'boston' in text:  # Colour then word ie(yellow Press)
            text = text.replace('button ', '').replace('boston ', '')
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

        elif "on 1st 1" in text.replace('one', '1') or "on first 1" in text.replace('one', '1'):
            # Word on screen, then word on told button
            text = text.replace("on first 1 ", '').replace("on 1st 1 ", '').replace("on first one ", '')\
                .replace("on 1st one ", '')
            OnFirst.onfirst(text)

        elif "on 1st 2" in text.replace('to', '2').replace('too', '2').replace('two', '2') \
                or "on first 2" in text.replace('to', '2').replace('too', '2').replace('two', '2'):
            text = text.replace('to', '2').replace('too', '2').replace('two', '2')
            text = text.replace("on 1st 2 ", '').replace("on first 2 ", '')

            answer = OnFirst.onfirstwords(text)
            if answer != "Not a Word":
                p = multiprocessing.Process(target=speak, args=(answer,))
                p.start()

                while p.is_alive():
                    listen = get_audio()
                    if listen == 'stop':
                        p.terminate()
            else:
                speak(answer)

        elif 'reset memory' in text:
            Memory.resetmemstage()
            speak('Memory reset')

        elif 'memory' in text:  # Number on screen, then buttons
            text = text.replace('to', '2').replace('too', '2').replace('two', '2')\
                .replace('for ', '4').replace('memory ', '').replace('at', '').replace('-', '')\
                .replace('0', '').replace(' ', '')
            Memory.memory(text)

        elif 'reset morse' in text:
            Morse.resetmorse()
            speak('Morse reset')

        elif 'morse' in text:  # Sets of flashes ie(dot dot dash) or (0 0 1)
            text = text.replace('morse ', '')
            Morse.morse(text)

        elif 'complex wires' in text:  # Wire attributes separated by 'next' ie(red star next blue)
            text = text.replace('complex wires ', '').replace('read', 'red')
            CompWires.compwires(text)

        elif 'sequence' in text or 'sequins' in text:  # colour then letter sep by 'next' ie(red alpha next blue bravo)
            text = text.replace('sequins ', '').replace('sequence ', '')
            WireSequence.sequence(text)

        elif 'reset sequence' in text:
            WireSequence.resetsequence()
            speak('Sequence Reset')

        elif 'maze' in text or 'maize' in text or "may's" in text:  #
            # 1 Indicator, start, finish sep by 'next' ie(44 next 43 next 55)
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
        elif 'add strike' in text or "i'd strike" in text:
            BombSetup.addstrike()

        elif 'remove strike' in text:
            BombSetup.removestrike()

        elif 'bomb status' in text:
            BombSetup.bomb_status()

        elif text == 'the bomb is complete':
            speak('We did it')
            total_reset()

        elif 'we blew up' in text:
            speak("It's Not my Fault... i'm the bot")
            total_reset()

        elif 'bomb reset' in text:
            total_reset()

        elif 'exit program' in text:
            speak('Goodbye')
            break
