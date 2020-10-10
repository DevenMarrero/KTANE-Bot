from Voice import speak, get_audio


def onfirst(text):
    word = text.lower()

    if text == 'empty':
        speak('Bottom Left')

    elif 'blank' in text:
        speak('Middle Right')

    elif word == 'charlie':
        speak('Top Right')

    elif text == 'cc':
        speak('Bottom Right')

    elif text == 'display':
        speak('Bottom Right')

    elif text == 'first':
        speak('Top Right')

    elif text == 'hold on':
        speak('Bottom Right')

    elif text == 'lead':
        speak('Bottom Right')

    elif text == 'led':
        speak('Middle Left')

    elif text == 'lead to':
        speak('Bottom Left')

    elif text == 'no':
        speak('Bottom Right')

    elif text == 'nothing':
        speak('Middle Left')

    elif text == 'okay':
        speak('Top Right')

    elif text == 'read':
        speak('Middle Right')

    elif text == 'red':
        speak('Middle Right')

    elif text == 'read plant':
        speak('Bottom Left')

    elif text == 'says':
        speak('Bottom Right')

    elif word == 'c' or word == 'see':
        speak('Bottom Right')

    elif text == 'their india':
        speak('Middle Right')

    elif text == 'there':
        speak('Bottom Right')

    elif text == "they are apostrophe":
        speak('Bottom Left')

    elif text == 'they are':
        speak('Middle Left')

    elif text == 'you are letters':
        speak('Top Left')

    elif text == 'yes':
        speak('Middle Left')

    elif text == 'you':
        speak('Middle Right')

    elif text == 'your':
        speak('Middle Right')

    elif text == 'you are':
        speak('Bottom Right')

    elif text == 'you are apostrophe':
        speak('Middle Right')

    else:
        speak('That is not a word')
        return
    onfirstwords()


def onfirstwords():
    text = get_audio()
    text = text.lower()

    if text == 'blank':
        speak("WAIT... RIGHT... OKAY... MIDDLE... BLANK")

    elif text == 'done':
        speak("SURE... h u h... NEXT... WHAT, Question... YOUR...u r... your apostrophe... HOLD... LIKE... YOU... "
              "U letter... "
              "YOU ARE... U h... DONE")

    elif text == 'first':
        speak("LEFT... OKAY... YES... MIDDLE... NO... RIGHT... NOTHING... u3h... MIDDLE... WAIT... READY... BLANK... "
              "WHAT... PRESS... FIRST")

    elif text == 'hold':
        speak("YOU ARE... U letter... DONE... U h... YOU...u r... SURE... what question... READY... BLANK... WHAT... "
              "PRESS FIRST")

    elif text == 'left':
        speak("RIGHT... LEFT")

    elif text == 'like':
        speak("your apostrophe... NEXT... U letter...u r... HOLD... DONE... U h... what question... h u h... YOU... "
              "LIKE")

    elif text == 'middle':
        speak("BLANK... READY... OKAY... what question... NOTHING... PRESS... NO... WAIT... LEFT... MIDDLE")

    elif text == 'next':
        speak("WHAT... h u h... U h... YOUR... HOLD... SURE... NEXT")

    elif text == 'no':
        speak("BLANK... u3h... WAIT... FIRST... WHAT... READY... RIGHT... YES... NOTHING... LEFT... PRESS... OKAY... "
              "NO")

    elif text == 'nothing':
        speak("u3h... RIGHT... OKAY... MIDDLE... YES... BLANK... NO... PRESS... LEFT... WHAT... WAIT... FIRST... "
              "NOTHING")

    elif text == 'okay':
        speak("MIDDLE... NO... FIRST... YES... u3h... NOTHING... WAIT... OKAY")

    elif text == 'press':
        speak("RIGHT... MIDDLE... YES... READY... PRESS")

    elif text == 'ready':
        speak("YES... OKAY... WHAT... MIDDLE... LEFT... PRESS... RIGHT... BLANK... READY")

    elif text == 'right':
        speak("YES... NOTHING... READY... PRESS... NO... WAIT... WHAT... RIGHT")

    elif text == 'sure':
        speak("YOU ARE... DONE... LIKE... your apostrophe... YOU... HOLD... h u h...u r... SURE")

    elif text == 'you letter':
        speak("h u h... SURE... NEXT... what question... your, apostrophe...u r... U h... DONE... U")

    elif text == 'you are letters':
        speak("DONE... U letter... UR")

    elif text == 'h u h':
        speak("h u h")

    elif text == 'u h':
        speak("UR... U, letter... YOU ARE... your, apostrophe... NEXT... U h")

    elif text == 'u3h':
        speak("READY... NOTHING... LEFT... WHAT... OKAY... YES... RIGHT... NO... PRESS... BLANK... u3h")

    elif text == 'wait' or text == 'weight':
        speak("U3h... NO... BLANK... OKAY... YES... LEFT... FIRST... PRESS... WHAT... WAIT")

    elif text == 'what':
        speak("u3h... WHAT")

    elif text == 'what question':
        speak("YOU... HOLD... your, apostrophe... YOUR... YOU... DONE... UH UH... LIKE... YOU ARE... h u h...u r... "
              "NEXT...what question")

    elif text == 'yes':
        speak("OKAY... RIGHT... u3h... MIDDLE... FIRST... WHAT... PRESS... READY... NOTHING... YES")

    elif text == 'you':
        speak("SURE... YOU ARE... YOUR... your, apostrophe... NEXT... h u h... U R... HOLD... what question... YOU")

    elif text == 'your':
        speak("U H... YOU ARE... h u h... YOUR...")

    elif text == "you are apostrophe":
        speak("YOU... your, apostrophe")

    elif text == 'you are':
        speak("YOUR... NEXT... LIKE... H U H... what question... DONE... U H... HOLD... U letter... your apostrophe"
              "... SURE...u r... YOU ARE")
    else:
        speak('not a word')
        onfirstwords()
