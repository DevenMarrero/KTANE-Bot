from Voice import speak
stage = 1


def memory(s):
    screen = []
    for i in s:
        screen.append(i)

    global stage
    global sonepos
    global sonelabel
    global stwopos
    global stwolabel
    global sthreepos
    global sthreelabel
    global sfourpos
    global sfourlabel
    
    if not len(screen) == 5:
        speak('Not enough numbers')
        return
    
    else:
        if stage == 1:

            if int(screen[0]) == 1:
                speak('Position 2')
                sonepos = 2
                sonelabel = screen[sonepos]  # 2

            elif int(screen[0]) == 2:
                speak('Position 2')
                sonepos = 2
                sonelabel = screen[sonepos]

            elif int(screen[0]) == 3:
                speak('Position 3')
                sonepos = 3
                sonelabel = screen[sonepos]

            else:
                speak('Position 4')
                sonepos = 4
                sonelabel = screen[sonepos]

        elif stage == 2:

            if int(screen[0]) == 1:
                speak('Labeled "4"')
                stwopos = str(screen.index('4'))  # 4
                stwolabel = 4

            elif int(screen[0]) == 2:
                speak('Position ' + str(sonepos))
                stwopos = sonepos
                stwolabel = screen[stwopos]

            elif int(screen[0]) == 3:
                speak('Position 1')
                stwopos = 1
                stwolabel = screen[stwopos]

            else:
                speak('Position ' + str(sonepos))
                stwopos = sonepos
                stwolabel = screen[stwopos]

        elif stage == 3:

            if int(screen[0]) == 1:
                speak(f'Labeled "{stwolabel}"')
                sthreepos = str(screen.index(str(stwolabel)))
                sthreelabel = stwolabel

            elif int(screen[0]) == 2:
                speak(f'Labeled "{sonelabel}"')
                sthreepos = str(screen.index(str(sonelabel)))
                sthreelabel = sonelabel

            elif int(screen[0]) == 3:
                speak('Position 3')
                sthreepos = 3
                sthreelabel = screen[sthreepos]

            else:
                speak('Labeled "4"')
                sthreepos = str(screen.index('4'))
                sthreelabel = 4

        elif stage == 4:

            if int(screen[0]) == 1:
                speak(f'position {sonepos}')
                sfourpos = sonepos
                sfourlabel = screen[sfourpos]

            elif int(screen[0]) == 2:
                speak(f'Position 1')
                sfourpos = 1
                sfourlabel = screen[sfourpos]

            elif int(screen[0]) == 3:
                speak(f'Position {stwopos}')
                sfourpos = stwopos
                sfourlabel = screen[sfourpos]

            else:
                speak(f'Position {stwopos}')
                sfourpos = stwopos
                sfourlabel = screen[int(sfourpos)]

        else:
            
            if int(screen[0]) == 1:
                speak(f'Labeled "{sonelabel}"')

            elif int(screen[0]) == 2:
                speak(f'Labeled "{stwolabel}"')

            elif int(screen[0]) == 3:
                speak(f'Labeled "{sfourlabel}"')

            else:
                speak(f'Labeled "{sthreelabel}"')
        stage += 1


def resetmemstage():
    global stage
    stage = 1
