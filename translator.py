from googletrans import Translator
import speech_recognition as sr

class Trans():
    def __init__(self, main_linguage, go_to) -> None:
        self.main_language =  main_linguage
        self.go_to = go_to

    def translator_text(self, text:str):
        translator = Translator()
        text_trans = translator.translate(text, dest=self.go_to)
        return text_trans.text

    def listen_and_convert(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language=self.main_language)
                return text
            except sr.UnknownValueError:
                print("Unable to understand the audio")
