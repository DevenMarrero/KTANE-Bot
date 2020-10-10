from Voice import speak, get_audio

import Knobs
import CompWires
import OnFirst
import WireSequence
import Memory
import Maze
import Button
import Setup
import Password
import Morse
import KeyPad
import SimpleWires
import Simon
# fix attribute error
# Stop for OnFirst

while 1:
    text = get_audio()
    text = text.replace('fuse', 'diffuse').replace("Moore's", 'Morse').replace("/", '').lower()

    # Modules
    if 'wires' in text:  # Name all wires. ie(red, blue, red)
        text = text.replace('.', '').replace('wires ', '')
        SimpleWires.simplewires(text)

    elif 'button' in text:  # Colour then word ie(yellow Press)
        text = text.replace('button ', '')
        Button.button(text)

    elif 'strip' in text:  # Color ie(Red)
        text = text.replace('strip ', '')
        Button.holdbutton(text)

    elif 'keypad' in text or 'symbols' in text:  # Say symbols
        text = text.replace('keypad ', '').replace('symbols ', '')
        KeyPad.keypad(text)

    elif 'simon' in text:  # Say colours ie(Red, Red, Blue)
        text = text.replace('simon ', '')
        Simon.simon(text)

    elif "words" in text or "on 1st" in text:  # Word on screen, then word on told button
        text = text.replace("words ", '').replace("on first ", '')
        OnFirst.onfirst(text)

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

    elif 'sequence' in text or 'sequins' in text:  # colour then letter separated by 'next' ie(red charlie next blue bravo)
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

    # Commands
    elif 'run setup' in text:
        Setup.setup()

    elif 'add strike' in text:
        Setup.addstrike()

    elif 'remove strike' in text:
        Setup.removestrike()

    elif 'the bomb is complete' in text:
        speak('We did it')
        break

    elif 'we blew up' in text:
        speak("It's Not my Fault")
        break
