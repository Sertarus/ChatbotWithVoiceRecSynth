# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr


def voice_rec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        return r.recognize_vosk(audio)
    except sr.UnknownValueError:
        print("Vosk could not understand audio")
    except sr.RequestError as e:
        print("Vosk error; {0}".format(e))


def text_to_speech(text):
    return text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(text_to_speech(voice_rec()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
