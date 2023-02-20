import time
from tkinter import *
from tkinter import messagebox
from english_words import get_english_words_set
import random
import keyboard
import math


class Screen:

    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed App")
        self.window.minsize(150, 150)
        self.window.config(padx=30, pady=10, bg="#000000")

        self.label = Label()
        self.entry_field = Entry()
        self.entry = Entry()
        self.timer_text = None
        self.keyboard = True
        self.time = None
        # self.countdown = False

        self.set_of_words = []
        self.written_words = []
        self.text = ""
        self.entry_txt = ""
        self.spelling = []
        self.spelling_points = 0
        self.words_points = 0

        self.create_widgets()
        self.window.mainloop()

    def create_text_easy(self):
        self.clear_screen()
        with open("common_english_words.txt", "r") as text:
            all_text = text.read()
            words = list(map(str, all_text.split()))
            for word in range(12):
                self.set_of_words.append(random.choice(words))
            self.label = Label(self.window, text=f"{self.change_into_txt(self.set_of_words).lower()}", fg="#fafafa",
                               bg="#000000", font=("Arial", 20, "bold"), wraplength=600)
            self.label.grid(column=0, row=2, rowspan=3, columnspan=2)

    def create_text_hard(self):
        self.clear_screen()
        for word in range(10):
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
        self.spelling_points = 0
        self.window.update()

    def text_callback(self, var, index, mode):
        # print("Written {}".format(self.entry_field.get()))
        self.entry_txt = self.entry_field.get()
        self.check_spelling()
        self.start_timer()

    def backspace(self, event):
        try:
            self.spelling.pop()
            self.spelling_points = self.count_points()
            return self.spelling, self.spelling_points
        except IndexError:
            pass

    def count_points(self):
        points = 0
        for check in self.spelling:
            if check == "ok":
                points += 1
            else:
                pass
        if len(self.spelling) == 0:
            points = 0
        return points

    # def count_words(self):
    #     # if keyboard.read_key() == "space":
    #     #     self.words_points += 1
    #     pass

    def check_spelling(self):
        letters = []
        letters_string = ""
        try:
            for letter in self.entry_txt:
                letters.append(letter)
                letters_string = ''.join(letters)
            self.written_words = letters_string.split(" ")
            self.words_points = len(self.written_words)
            if keyboard.read_key() != "backspace":
                if letters_string[len(letters_string) - 1] == self.text[len(letters_string) - 1]:
                    self.spelling.append("ok")
                    self.spelling_points = self.count_points()
                else:
                    self.spelling.append("wrong")
                    self.spelling_points = self.count_points()

        except IndexError:
            pass

        print(self.spelling)
        print(letters_string)
        print(self.spelling_points)
        print(self.words_points)
        print(self.written_words)

    def count_down(self, count):
        if count >= 0:
            self.time = self.window.after(1000, self.count_down, count-1)
            self.timer_text['text'] = count
        else:
            self.window.after_cancel(self.time)
            messagebox.showinfo("End", f"Yor CPM is {int(self.spelling_points)},"
                                       f" your WPM is {int(len(self.written_words))}.")

    def start_timer(self):
        countdown = len(self.entry_txt) == 1
        if countdown:
            self.count_down(60)
        elif len(self.entry_txt) == len(self.text):
            messagebox.showinfo("End", f"Yor CPM is {int((self.spelling_points * 60)/ int(self.timer_text['text']))},"
                                       f" your WPM is "
                                       f"{int((len(self.written_words) * 60) / int(self.timer_text['text']))}.")

    def count_score(self):
        pass

    def save_score(self):
        pass
    #
    # def restart(self):
    #     self.window.after_cancel(self.time)

    def create_widgets(self):
        # timer
        # seconds = IntVar()
        # seconds.set(60)
        self.timer_text = Label(text="60", fg="#fafafa", bg="#000000", font=("Arial", 12))
        self.timer_text.grid(column=0, row=0)
        # characters per minute
        # words per minute
        # mistakes
        # current highest score
        # text label
        easy = Button(text="Easy Mode", font=("Arial", 12), bg="#000000", fg="#fafafa", command=self.create_text_easy)
        easy.grid(column=0, row=1)
        hard = Button(text="Hard Mode", font=("Arial", 12), bg="#000000", fg="#fafafa", command=self.create_text_hard)
        hard.grid(column=3, row=1)
        # entry field
        entry_label = Label(text="Write Below", width=15, bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
        entry_label.grid(column=0, row=5)
        self.entry = StringVar()
        self.entry.trace_add('write', self.text_callback)
        self.entry_field = Entry(self.window, width=100, textvariable=self.entry, bg="#242424", fg="#fafafa")
        self.entry_field.grid(column=0, row=6, columnspan=4)
        self.entry_field.bind("<BackSpace>", self.backspace)

        # restart button
        # restart = Button(text="Restart", font=("Arial", 12), bg="#000000", fg="#fafafa",
        #                  command=lambda: [self.restart(), self.clear_screen()])
        # restart.grid(column=2, row=2)
        # exit button
