# This is a sample Python script.
import soundfile
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
from TTS.api import TTS
import pyaudio
import wave
from chatterbot import ChatBot
from spacy.cli.download import download



def play_voice():
    chunk = 1024
    f = wave.open("output.wav", "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


def voice_rec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print(r.recognize_vosk(audio))
    try:
        return r.recognize_vosk(audio)
    except sr.UnknownValueError:
        print("Vosk could not understand audio")
    except sr.RequestError as e:
        print("Vosk error; {0}".format(e))


def text_to_speech(text):
    print(TTS().list_models())
    tts = TTS("tts_models/multilingual/multi-dataset/your_tts")
    tts.tts_to_file(text=text,
                    speaker_wav="target/speaker4.wav", language="en", file_path="output.wav")
    play_voice()

def get_text(text):
    chatbot = ChatBot("Alina")
    state = chatbot.get_response(text)
    return str(state)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #text_to_speech(get_text(voice_rec()))
    print(get_text("hello"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
