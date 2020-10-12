# Keep Talking and Nobody Explodes Expert Bot

![](https://media.playstation.com/is/image/SCEA/keep-talking-and-nobody-explodes-ps4-us-screen-04-13oct16?$MediaCarousel_Original$)

## Description
This is a Python bot built to act as the 'expert' and your diffusal teammate for the Game [Keep Tallking and Nobody Explodes](https://store.steampowered.com/app/341800/Keep_Talking_and_Nobody_Explodes/)

For the unfamiliar, this is a 2+ player game where one player sits at a computer and describes a bomb only they can see to the experts. 
The experts must then quickly flip through their multi-page [manual](https://bombmanual.com/) and use the information provided to help the diffuser safely diffuse the bomb.

## Installation- Windows Only
**Python Clone**

Install Libraries

`pip install gTTS`

`pip install SpeechRecognition`

`pip install playsound`

Run `Bot.py` to use

**.EXE Download- Found in EXE Branch**

Open downloaded folder and run `Bot.exe`

# Commands

Commands are spoken and must follow wording/format provided.
I tried to make the commands as intuative as possible but let me know if I should make some changes.

### Bomb Variables 

All values will default to 0 or False. 
```
Batteries <#>            -Number of batteries
Serial <vowel> <even>    -Say vowel if there is a vowel and likewise for even, ie: `serial vowel even` or `serial vowel`
Indicators <car> <freak> -Similar to Serial, say what indicators are lit, ie: "Indicators freak"
Parallel port <>         -Say command if there is a port, otherwise don't say it
```

### Bomb Control

```
Add Strike           -Adds strike to bomb
Remove Strike        -Removes strike from bomb
bomb reset           -Resets the bomb to try again
The bomb is complete -Happy celebration, also resets bomb
We blew up           -Denial, also resets bomb
exit program         -Closes bot
```

### Simple Wires

`Simple Wires <wires> -Name all colours of wires (red, blue, yellow, black, white)`

Example:

`Simple Wires Red Blue Red Black`

### Button

Step 1

`Button <colour, word> -Colour of the button then word displayed`

**If holding**

`Strip <colour> -Colour of LED strip`

### KeyPad

`Keypad <symbols>`

![image](https://user-images.githubusercontent.com/70239160/95711600-f9d1f600-0c17-11eb-83e3-d99d24c6793b.png)

```
Ballon      Euro     Copyright     six     Trident     six

Alpha     Ballon     Nose     Paragraph     Smile     Euro

Lambda     Charlie     Cursive     Bravo     Bravo     Puzzle

Lightning     Cursive     Butterfly     kitty     Charlie     Smash

Kitty     Star     Semicolon     ButterFly     Paragraph     Trident

Hotel     Hotel     Lambda    Question     Three     November

Charlie     Question     Star     Smile     Star     Omega
```

### Simon Says

`simon <colours> -Coloured Flashes in oder (Blue, Yellow, Green, Red)`

Example:

`Simon Red Red Blue`

### Who's On First

**Step 1**

`On First <word> -Word on display`

**Step 2**

Ridirected autimatically from step 1

When the bot reads out the possible buttons say 'Stop' to save time and continue

`<Word> -Word on button from step 1`

Here is a table of what you will have to say for each word to not mix up the bot

```
' '      - Empty
blank    - blank
c        - Charlie
cee      - c c 
display  - display
done     - done
first    - first
hold     - hold
hold on  - hold on
lead     - lead
led      - L. E. D.
leed     - lead to
left     - left
like     - like
middle   - middle
next     - next
no       - no
nothing  - nothing
okay     - okay
press    - press
read     - read
red      - red
reed     - read plant
ready    - ready
says     - says
see      - see
sure     - sure
their    - there India
there    - there
they're  - they are apostrophy
they are - they are
u        - you letter
ur       - you are letters
uh huh   - h u h
uh uh    - uh
uhhh     - u3h
wait     - wait
what     - what
what?    - what question
yes      - yes
you      - you
your     - your
you're   - you are apostrophy
you are  - you are
```

### Memory

`memory <display> <button numbers from left to right>`

Example:

```
   2
3 1 2 4
```

`memory 2 3 1 2 4`

If there is more than one memory module make sure to reset memory

`reset memory`

### Morse Code

`morse <0/1 for letter> -0 is short(dot) and 1 is long(dash)`

How to Use:

- Letters must be givin 1 at a time
- Minimum of 2 letters required
- Letters do not have to be in order
- Bot Will tell you if you need more letters

Example:

`-... ... -.-.`

```
morse 1 0 0 
morse 0 0 0 
morse 1 0 1 0
```

If there is more than one morse module make sure to reset morse

`reset morse`

### Complex Wires

`complicated <wires> - Wire attributes include (Red, Blue, Star, Light, None)`

Seperate wires with the word 'next' None/black is for wires with no attributes

Example:

```
4 Wires:
Red
Blue with Star
Red/Blue with Light/Star
No attributes
```

`complicated red next blue star next red blue star light next none`

### Wire Sequence

Wires go from top to bottom separated by 'next'

`sequence <colour> <destination> -where color in (red, blue, black) and destination in (alpha, bravo, charlie)`

Example:

```
1 -blue-- A

2 -red--- C

3 -black- B
```

`sequence blue alpha next red charlie next black bravo`

If there is more than one sequence module make sure to reset sequence

`reset sequence`

### Maze

Coords start at upper left (1, 1) and go horizontally then vertically.

`maze <coords> - Where coords are 3 pairs of numbers for indicator, start, finish separated by 'next'`

Example:

```
X X X X
S X O X
X X X X
X X X F

Indicator - (3, 2)
Start     - (1, 2)
Finish    - (4, 4)
```

`maze 3 2 next 1 2 next 4 4`

### Password

This module requires fast thinking or a good memory of the NATO Alphabet

`password <letters>` - Letters in row 1 and 3 separated by next

How to Use:

Scroll through the 1st row of letters and say a word that start with the letter you see. The word does not have to be in the NATO Alphabet, 'A' can be alpha, apple, or even alligator.

Say next and do the same with the 3rd row of letters.

Example:

```
t k e n
f h r k
x i e y
```

`password them fox x-ray next every round echo`

### Needy- Knobs

`knobs <LED's> - Coloumns with both LED's Lit`

Example - 1 is on 0 is off:

```
1 0 1 1
0 1 1 1
```

`knobs 3 4`
