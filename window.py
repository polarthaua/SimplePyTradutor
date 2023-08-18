import customtkinter as ctk
from translator import Trans

class Window:
    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.geometry("700x400")
        self.window.title("Py-Translator")
        self.main_language, self.go_language = "pt-br", "en"
        self.transla = Trans(self.main_language, self.go_language)
        self.response_label = self.language_entry = self.whatis_language_label = None

    def draw(self):
        speak_button = ctk.CTkButton(self.window, text="Speak", command=self.tranlator_speak, anchor=ctk.CENTER)
        self.language_entry = ctk.CTkEntry(self.window)
        language_label = ctk.CTkLabel(self.window, text="Write your \
language first and then which language you will translate to\nEx: pt-br en")

        self.whatis_language_label = ctk.CTkLabel(self.window, text=f"From: {self.main_language}\n To: {self.go_language}")

        language_label.pack(padx=10, pady=10)
        self.language_entry.pack(padx=10, pady=10)
        speak_button.pack(padx=10, pady=10)
        self.whatis_language_label.pack(padx=10, pady=10)
        self.language_entry.bind("<Return>", self.on_entry_return)

    def on_entry_return(self, event):
        input_text = self.language_entry.get()
        self.main_language, self.go_language = input_text.split()[0], input_text.split()[1]
        self.transla = Trans(self.main_language, self.go_language)
        self.whatis_language_label.configure(text=f"From: {self.main_language}\n To: {self.go_language}")

    def tranlator_speak(self):
        text_response = self.transla.listen_and_convert()
        text_response = self.transla.translator_text(text_response)
        if self.response_label:
            self.response_label.configure(text=text_response)
        else:
            self.response_label = ctk.CTkLabel(self.window, text=text_response)
            self.response_label.pack(padx=10, pady=10)

    def main(self):
        self.draw()
        self.window.mainloop()