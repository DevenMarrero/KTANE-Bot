# Keep Talking and Nobody Explodes Expert Bot

![](https://media.playstation.com/is/image/SCEA/keep-talking-and-nobody-explodes-ps4-us-screen-04-13oct16?$MediaCarousel_Original$)

## Description
This is a Python bot built to act as the 'expert' and your diffusal teammate for the Game [Keep Tallking and Nobody Explodes](https://store.steampowered.com/app/341800/Keep_Talking_and_Nobody_Explodes/)

For the unfamiliar this is a 2+ player game where one player sits at a computer and describes a bomb only they can see to the experts. 
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
Batteries <#>          -Number of batteries
Serial <vowel/even>    -Say vowel if there is a vowel and likewise for even, ie: "Serial, vowel even"
Indicators <car/freak> -Similar to Serial, say what indicators are lit, ie: "Indicators freak"
Parallel port <>       -Say command if there is a port, otherwise don't say it
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

`Button <colour, word> -Colour of the button then word displayed`

Example:

`Button Yellow Detonate`

### Strip

LED Strip that lights up after holding button

`Strip <colour> -Colour of LED strip`

### KeyPad

`Keypad <symbols> -All 4 keypad symbols`

![image](https://user-images.githubusercontent.com/70239160/95704097-a0ac9700-0c04-11eb-9b25-77e9aa50c138.png)

`Ballon, Alpha, Lambda, Lightning, Kitty, Hotel, Charlie`

![image](https://user-images.githubusercontent.com/70239160/95704191-dbaeca80-0c04-11eb-93e2-fc0db738327a.png)

`Euro, Ballon, Charlie, Cursive, star, Hotel, Question`

![image](https://user-images.githubusercontent.com/70239160/95704238-0862e200-0c05-11eb-9b90-30cc21e6c74a.png)

`Copyright, nose, cursive, butterfly, semicolon, lambda, star`

![image](https://user-images.githubusercontent.com/70239160/95704290-33e5cc80-0c05-11eb-8546-ad4ad26348ee.png)

`Six, Paragraph, Bravo, Kitty, Butterfly, Question, Smile/Smiley`

![image](https://user-images.githubusercontent.com/70239160/95704393-858e5700-0c05-11eb-84c3-f4b820e21b99.png)

`Trident, Smile, Bravo, Charlie, Paragraph, Three`

![image](https://user-images.githubusercontent.com/70239160/95704690-968b9800-0c06-11eb-8669-b85523ce30d5.png)

`Six, Euro, Puzzle, Smash, Trident, November, Omega`


### Simon Says

`simon <colours> -Coloured Flashes in oder (Blue, Yellow, Green, Red)`

Example:

`Simon Red Red Blue`

### Who's On First

**Step 1**

`On First <word> -Word on display`

**Step 2**

Ridirected autimatically from step 1

`<Word> -Word on button from step 1`

Here is a table of what you will have to say for each word to not mix up the bot

```
' '     - Empty
blank   - blank
c       - Charlie
cee     - c c 
display - display
done - done
first - first
hold - hold
hold on - hold on
lead - lead
led - L. E. D.
leed - lead to
left - left
like - like
middle - middle
next - next
no - no
nothing - nothing
okay - okay
press - press
read - read
red - red
reed - read plant
ready - ready
says - says
see - see
sure - sure
their - there India
there - there
they're - they are apostrophy
they are - they are
u - you letter
ur - you are letters
uh huh - h u h
uh uh - uh
uhhh - u3h
wait - wait
what - what
what? - what question
yes - yes
you - you
your - your
you're - you are apostrophy
you are - you are
```
