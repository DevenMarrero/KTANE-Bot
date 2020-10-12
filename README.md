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

### Bomb Commands

```
Add Strike           -Adds strike to bomb
Remove Strike        -Removes strike from bomb
bomb reset           -Resets the bomb to try again
The bomb is complete -Happy celebration, also resets bomb
We blew up           -Denial, also resets bomb
exit program         -Closes bot
```
