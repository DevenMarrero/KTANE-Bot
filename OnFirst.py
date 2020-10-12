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

    if 'blank' in text:
        answer = "WAIT... RIGHT... OKAY... MIDDLE... BLANK"

    elif 'done' in text:
        answer = "SURE... h u h... NEXT... WHAT, Question... YOUR...u r... your apostrophe... HOLD... LIKE... YOU... " \
                 "U letter... " \
                 "YOU ARE... U h... DONE"

    elif 'first' in text:
        answer = "LEFT... OKAY... YES... MIDDLE... NO... RIGHT... NOTHING... u3h... MIDDLE... WAIT... READY... " \
                 "BLANK... WHAT... PRESS... FIRST"

    elif 'hold' in text:
        answer = "YOU ARE... U letter... DONE... U h... YOU...u r... SURE... what question... READY... " \
                 "BLANK... WHAT... PRESS FIRST"

    elif 'left' in text:
        answer = "RIGHT... LEFT"

    elif 'like' in text:
        answer = "your apostrophe... NEXT... U letter...u r... HOLD... DONE... U h... what question... h u h... YOU... "\
                 "LIKE"

    elif 'middle' in text:
        answer = "BLANK... READY... OKAY... what question... NOTHING... PRESS... NO... WAIT... LEFT... MIDDLE"

    elif 'next' in text:
        answer = "WHAT... h u h... U h... YOUR... HOLD... SURE... NEXT"

    elif 'no' in text:
        answer = "BLANK... u3h... WAIT... FIRST... WHAT... READY... RIGHT... YES... NOTHING... LEFT... " \
                 "PRESS... OKAY... NO"

    elif 'nothing' in text:
        answer = "u3h... RIGHT... OKAY... MIDDLE... YES... BLANK... NO... PRESS... LEFT... WHAT... WAIT... FIRST... "\
                 "NOTHING"

    elif 'okay' in text:
        answer = "MIDDLE... NO... FIRST... YES... u3h... NOTHING... WAIT... OKAY"

    elif 'press' in text:
        answer = "RIGHT... MIDDLE... YES... READY... PRESS"

    elif 'ready' in text:
        answer = "YES... OKAY... WHAT... MIDDLE... LEFT... PRESS... RIGHT... BLANK... READY"

    elif 'right' in text:
        answer = "YES... NOTHING... READY... PRESS... NO... WAIT... WHAT... RIGHT"

    elif 'sure' in text:
        answer = "YOU ARE... DONE... LIKE... your apostrophe... YOU... HOLD... h u h...u r... SURE"

    elif 'you letter' in text:
        answer = "h u h... SURE... NEXT... what question... your, apostrophe...u r... U h... DONE... U"

    elif 'you are letters' in text:
        answer = "DONE... U letter... UR"

    elif 'huh' in text.strip():
        answer = "h u h"

    elif 'uh' in text.strip():
        answer = "UR... U, letter... YOU ARE... your, apostrophe... NEXT... U h"

    elif 'u3h' in text.strip():
        answer = "READY... NOTHING... LEFT... WHAT... OKAY... YES... RIGHT... NO... PRESS... BLANK... u3h"

    elif 'wait' in text or 'weight' in text:
        answer = "U3h... NO... BLANK... OKAY... YES... LEFT... FIRST... PRESS... WHAT... WAIT"

    elif 'what' in text:
        answer = "u3h... WHAT"

    elif 'what question' in text:
        answer = "YOU... HOLD... your, apostrophe... YOUR... YOU... DONE... UH UH... LIKE... YOU ARE... h u h...u r... "\
                 "NEXT...what question"

    elif 'yes' in text:
        answer = "OKAY... RIGHT... u3h... MIDDLE... FIRST... WHAT... PRESS... READY... NOTHING... YES"

    elif 'you' in text:
        answer = "SURE... YOU ARE... YOUR... your, apostrophe... NEXT... h u h... U R... HOLD... what question... YOU"

    elif 'your' in text:
        answer = "U H... YOU ARE... h u h... YOUR..."

    elif "you are apostrophe" in text:
        answer = "YOU... your, apostrophe"

    elif 'you are' in text:
        answer = "YOUR... NEXT... LIKE... H U H... what question... DONE... U H... HOLD... U letter... your apostrophe"\
                 "... SURE...u r... YOU ARE"
    else:
        return "Not a Word"
    return answer




