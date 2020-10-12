from Voice import speak, get_audio


def onfirst(text):
    word = text.lower()

    answer_dict = {
        'empty': 'Bottom Left',
        'blank': 'Middle Right',
        'charlie': 'Top Right',
        'cc': 'Bottom Right',
        'display': 'Bottom Right',
        'first': 'Top Right',
        'hold on': 'Bottom Right',
        'lead': 'Bottom Right',
        'led': 'Middle Left',
        'lead to': 'Bottom Left',
        'no': 'Bottom Right',
        'nothing': 'Middle Left',
        'okay': 'Top Right',
        'read': 'Middle Right',
        'red': 'Middle Right',
        'read plant': 'Bottom Left',
        'says': 'Bottom Right',
        'c': 'Bottom Right',
        'see': 'Bottom Right',
        'their india': 'Middle Right',
        'there': 'Bottom Right',
        'they are apostrophe': 'Bottom Left',
        'they are': 'Middle Left',
        'you are letters': 'Top Left',
        'yes': 'Middle Left',
        'you': 'Middle Right',
        'your': 'Middle Right',
        'you are': 'Bottom Right',
        'you are apostrophe': 'Middle Right',
    }
    print(word)
    if word in answer_dict:
        answer = answer_dict[word]

    else:
        speak('That is not a word')
        return False

    speak(answer)
    return True


def onfirstwords(text):
    text = text.lower()

    if text == 'blank':
        answer = "WAIT... RIGHT... OKAY... MIDDLE... BLANK"

    elif text == 'done':
        answer = "SURE... h u h... NEXT... WHAT, Question... YOUR...u r... your apostrophe... HOLD... LIKE... YOU... " \
                 "U letter... " \
                 "YOU ARE... U h... DONE"

    elif text == 'first':
        answer = "LEFT... OKAY... YES... MIDDLE... NO... RIGHT... NOTHING... u3h... MIDDLE... WAIT... READY... " \
                 "BLANK... WHAT... PRESS... FIRST"

    elif text == 'hold':
        answer = "YOU ARE... U letter... DONE... U h... YOU...u r... SURE... what question... READY... " \
                 "BLANK... WHAT... PRESS FIRST"

    elif text == 'left':
        answer = "RIGHT... LEFT"

    elif text == 'like':
        answer = "your apostrophe... NEXT... U letter...u r... HOLD... DONE... U h... what question... h u h... YOU... "\
                 "LIKE"

    elif text == 'middle':
        answer = "BLANK... READY... OKAY... what question... NOTHING... PRESS... NO... WAIT... LEFT... MIDDLE"

    elif text == 'next':
        answer = "WHAT... h u h... U h... YOUR... HOLD... SURE... NEXT"

    elif text == 'no':
        answer = "BLANK... u3h... WAIT... FIRST... WHAT... READY... RIGHT... YES... NOTHING... LEFT... " \
                 "PRESS... OKAY... NO"

    elif text == 'nothing':
        answer = "u3h... RIGHT... OKAY... MIDDLE... YES... BLANK... NO... PRESS... LEFT... WHAT... WAIT... FIRST... "\
                 "NOTHING"

    elif text == 'okay':
        answer = "MIDDLE... NO... FIRST... YES... u3h... NOTHING... WAIT... OKAY"

    elif text == 'press':
        answer = "RIGHT... MIDDLE... YES... READY... PRESS"

    elif text == 'ready':
        answer = "YES... OKAY... WHAT... MIDDLE... LEFT... PRESS... RIGHT... BLANK... READY"

    elif text == 'right':
        answer = "YES... NOTHING... READY... PRESS... NO... WAIT... WHAT... RIGHT"

    elif text == 'sure':
        answer = "YOU ARE... DONE... LIKE... your apostrophe... YOU... HOLD... h u h...u r... SURE"

    elif text == 'you letter':
        answer = "h u h... SURE... NEXT... what question... your, apostrophe...u r... U h... DONE... U"

    elif text == 'you are letters':
        answer = "DONE... U letter... UR"

    elif text.strip() == 'huh':
        answer = "h u h"

    elif text.strip() == 'uh':
        answer = "UR... U, letter... YOU ARE... your, apostrophe... NEXT... U h"

    elif text.strip() == 'u3h':
        answer = "READY... NOTHING... LEFT... WHAT... OKAY... YES... RIGHT... NO... PRESS... BLANK... u3h"

    elif text == 'wait' or text == 'weight':
        answer = "U3h... NO... BLANK... OKAY... YES... LEFT... FIRST... PRESS... WHAT... WAIT"

    elif text == 'what':
        answer = "u3h... WHAT"

    elif text == 'whatquestion':
        answer = "YOU... HOLD... your, apostrophe... YOUR... YOU... DONE... UH UH... LIKE... YOU ARE... h u h...u r... "\
                 "NEXT...what question"

    elif text == 'yes':
        answer = "OKAY... RIGHT... u3h... MIDDLE... FIRST... WHAT... PRESS... READY... NOTHING... YES"

    elif text == 'you':
        answer = "SURE... YOU ARE... YOUR... your, apostrophe... NEXT... h u h... U R... HOLD... what question... YOU"

    elif text == 'your':
        answer = "U H... YOU ARE... h u h... YOUR..."

    elif text == "you are apostrophe":
        answer = "YOU... your, apostrophe"

    elif text == 'you are':
        answer = "YOUR... NEXT... LIKE... H U H... what question... DONE... U H... HOLD... U letter... your apostrophe"\
                 "... SURE...u r... YOU ARE"
    else:
        speak('not a word')
        onfirstwords()
        return
    return answer




