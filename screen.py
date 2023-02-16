from tkinter import *
from english_words import get_english_words_set
import random


class Screen:

    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed App")
        self.window.minsize(150, 150)
        self.window.config(padx=50, pady=50, bg="#000000")

        self.label = Label()
        self.entry_field = Entry()
        self.entry = Entry()

        self.set_of_words = []
        self.text = ""
        self.entry_txt = ""
        self.spelling = []
        self.spelling_points = 0

        self.create_widgets()
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
        self.spelling.clear()
        self.entry_field.delete(0, END)

    def text_callback(self, var, index, mode):
        # print("Written {}".format(self.entry_field.get()))
        self.entry_txt = self.entry_field.get()
        self.check_spelling()

    def check_spelling(self):
        letters = []
        letters_string = ""
        try:
            # if len(self.entry.get()) < len(self.spelling):
            #     self.spelling_points -= 1
            #     self.spelling.pop()

            for letter in self.entry_txt:
                letters.append(letter)
                letters_string = ''.join(letters)

            if letters_string[len(letters_string) - 1] == self.text[len(letters_string) - 1]:
                self.spelling.append("ok")
                self.spelling_points += 1
            else:
                self.spelling.append("wrong")
                self.spelling_points -= 1

            print(self.spelling[-1])
            print(self.spelling)
            print(letters_string)
            print(self.spelling_points)
        except IndexError:
            print("First generate text!")

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
        entry_label = Label(text="Write Below", width=15, bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
        entry_label.grid(column=1, row=5)
        self.entry = StringVar()
        self.entry.trace_add('write', self.text_callback)
        self.entry_field = Entry(self.window, textvariable=self.entry, bg="#242424", fg="#fafafa")
        self.entry_field.grid(column=1, row=6, columnspan=2)
        # restart button
        # exit button
        pass
