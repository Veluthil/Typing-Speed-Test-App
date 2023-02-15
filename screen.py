from tkinter import *
from english_words import get_english_words_set
import random


class Screen:

    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed App")
        self.window.minsize(150, 150)
        self.window.config(padx=50, pady=50, bg="#000000")
        self.create_widgets()
        self.label = Label()

        self.set_of_words = []
        self.text = ""

        self.window.mainloop()

    def create_text_easy(self):
        self.clear_screen()
        with open("common_english_words.txt", "r") as text:
            all_text = text.read()
            words = list(map(str, all_text.split()))
            for word in range(17):
                self.set_of_words.append(random.choice(words))
            self.label = Label(self.window, text=f"{self.change_into_txt(self.set_of_words).lower()}", fg="#fafafa",
                               bg="#000000", font=("Arial", 20, "bold"), wraplength=600)
            self.label.grid(column=0, row=2, rowspan=3, columnspan=2)

    def create_text_hard(self):
        self.clear_screen()
        for word in range(11):
            self.set_of_words.append(random.choice(list(get_english_words_set(['web2'], lower=True))))
        self.label = Label(self.window, text=f"{self.change_into_txt(self.set_of_words)}", fg="#fafafa", bg="#000000",
                           font=("Arial", 20, "bold"), wraplength=600)
        self.label.grid(column=0, row=2, rowspan=3, columnspan=2)

    def change_into_txt(self, list_of_words):
        text = ' '.join(list_of_words)
        self.text = text
        return text

    def clear_screen(self):
        self.set_of_words.clear()
        self.text = ""
        self.label.destroy()

    def check_spelling(self):
        pass

    def count_time(self):
        pass

    def count_score(self):
        pass

    def save_score(self):
        pass

    def restart(self):
        pass

    def create_widgets(self):
        # timer
        # words per minute
        # mistakes
        # current highest score
        # text label
        easy = Button(text="Easy Mode", font=("Arial", 12), bg="#000000", fg="#fafafa", command=self.create_text_easy)
        easy.grid(column=0, row=1)
        hard = Button(text="Hard Mode", font=("Arial", 12), bg="#000000", fg="#fafafa", command=self.create_text_hard)
        hard.grid(column=1, row=1)
        # entry field
        # restart button
        # exit button
        pass
