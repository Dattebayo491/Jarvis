import pyttsx3
import speech_recognition

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def speachrecog():
    recog = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print('Слушаю вас...')
        recog.pause_threshold = 1
        recog.adjust_for_ambient_noise(mic)
        audio = recog.listen(mic, 10, 6)

    try:
        print('Распознаю вашу речь, секунду...')
        spk = recog.recognize_google(audio, language='ru')
        print(f"Вы сказали: {spk}")
    except Exception as error:
       print(f'Возникла ошибка: {error}')
       return ""
   
    return spk

text = speachrecog()

speak(text)