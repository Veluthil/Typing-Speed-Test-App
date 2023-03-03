from tkinter import *
from tkinter import messagebox
from english_words import get_english_words_set
import random
import keyboard


class Screen:

    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed App")
        self.window.minsize(150, 150)
        self.window.config(padx=30, pady=10, bg="#000000")

        self.easy = Button()
        self.hard = Button()
        self.difficulty_label = Label()
        self.generated_text = Text()
        self.entry_field = Entry()
        self.entry = Entry()
        self.timer_text = None
        self.keyboard = True
        self.time = None
        self.points = 0
        self.time_start = False
        self.count = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.set_of_words = []
        self.written_words = []
        self.text = ""
        self.entry_txt = ""
        self.spelling = []
        self.spelling_points = 0
        self.mistakes = 0
        self.words_points = 0
        self.net_wpm = 0
        self.difference = 0

        self.mist_value = Label()
        self.wpm_value = Label()
        self.cpm_value = Label()

        self.choose_difficulty()
        self.window.mainloop()

    def choose_difficulty(self):
        self.difficulty_label = Label(text="CHOOSE A DIFFICULTY", font=("Tahoma", 20, "bold"), bg="#000000", fg="#fafafa")
        self.difficulty_label.grid(column=0, row=0, columnspan=2, padx=50, pady=50)
        self.easy = Button(text="EASY", font=("Tahoma", 12, "bold"), bg="#000000", fg="#fafafa",
                           command=self.create_text_easy)
        self.easy.grid(column=0, row=1, padx=20, pady=20)
        self.hard = Button(text="HARD", font=("Tahoma", 12, "bold"), bg="#000000", fg="#fafafa",
                           command=self.create_text_hard)
        self.hard.grid(column=1, row=1, padx=20, pady=20)

    def create_text_easy(self):
        self.clear_screen()
        self.create_widgets()
        with open("common_english_words.txt", "r") as text:
            all_text = text.read()
            words = list(map(str, all_text.split()))
            for word in range(20):
                self.set_of_words.append(random.choice(words).lower())
            self.generated_text = Text(self.window, fg="#fafafa", bg="#000000", font=("Arial", 20, "bold"),
                                       height=4, width=50, wrap="word")
            self.generated_text.grid(column=0, row=2, rowspan=3, columnspan=8, pady=15)
            self.generated_text.insert(END, self.change_into_txt(self.set_of_words).lower())

    def create_text_hard(self):
        self.clear_screen()
        self.create_widgets()
        for word in range(20):
            self.set_of_words.append(random.choice(list(get_english_words_set(['web2'], lower=True))))
        self.generated_text = Text(self.window, fg="#fafafa", bg="#000000", font=("Arial", 20, "bold"),
                                   height=5, width=50, wrap="word")
        self.generated_text.grid(column=0, row=2, rowspan=3, columnspan=8, pady=15)
        self.generated_text.insert(END, self.change_into_txt(self.set_of_words))

    def change_into_txt(self, list_of_words):
        text = ' '.join(list_of_words)
        self.text = text
        return text

    def clear_screen(self):
        self.difficulty_label.destroy()
        self.set_of_words.clear()
        self.text = ""
        self.easy.destroy()
        self.hard.destroy()
        self.generated_text.destroy()
        self.spelling.clear()
        self.entry_field.delete(0, END)
        self.spelling_points = 0
        self.window.update()

    def text_callback(self, var, index, mode):
        self.entry_txt = self.entry_field.get()
        self.check_spelling()
        self.update_screen_board()
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

    def count_mistakes(self):
        mistakes = 0
        for check in self.spelling:
            if check == "wrong":
                mistakes += 1
            else:
                pass
        if len(self.spelling) == 0:
            mistakes = 0
        return mistakes

    def show_mistake(self, difference):
        entry_len = len(self.entry_txt) - 1 - difference
        self.generated_text.tag_config("#ff0000", foreground="#ff0000")
        char = self.entry_txt[len(self.entry_txt) - 1 - difference]
        self.generated_text.delete(f"1.{entry_len}", f"1.{entry_len + 1}")
        # char = self.set_of_words[self.words_points - 1][number]
        self.generated_text.insert(f"1.{entry_len}", char)
        self.generated_text.tag_add("#ff0000", f"1.{entry_len}")

    def show_correct(self, difference):
        entry_len = len(self.entry_txt) - 1 - difference
        self.generated_text.tag_config("#2AAA8A", foreground="#2AAA8A")
        char = self.text[len(self.entry_txt) - 1 - difference]
        self.generated_text.delete(f"1.{entry_len}", f"1.{entry_len + 1}")
        self.generated_text.insert(f"1.{entry_len}", char)
        self.generated_text.tag_add("#2AAA8A", f"1.{entry_len}")

    def show_original_letter(self):
        self.generated_text.tag_config("#fafafa", foreground="#fafafa")
        char = self.text[len(self.entry_txt)]
        self.generated_text.delete(f"1.{len(self.entry_txt)}")
        self.generated_text.insert(f"1.{len(self.entry_txt)}", char)
        self.generated_text.tag_add("#fafafa", f"1.{len(self.entry_txt)}")

    def check_spelling(self):
        letters = []
        letters_string = ""
        number = -1
        word = 0
        self.points = 0
        try:
            for letter in self.entry_txt.lower():
                if letter != " ":
                    self.points += 1
                    number += 1
                else:
                    word += 1
                    number = -1
                    # if len(self.written_words[word - 1]) < len(self.set_of_words[word - 1]):
                    #     self.lack = len(self.set_of_words[word - 1]) - len(self.written_words[word - 1])
                letters.append(letter)
                letters_string = ''.join(letters)
            self.written_words = letters_string.split(" ")
            self.words_points = len(self.written_words)
            if len(self.written_words[word]) > len(self.set_of_words[word]):
                number -= 1
                self.difference = len(self.written_words[word]) - len(self.set_of_words[word])
                self.written_words.pop()
                self.written_words.append(self.written_words[word][:-self.difference])
            if keyboard.read_key() != "backspace":
                if len(self.entry_txt) == len(self.text):
                    self.time_start = False
                    self.count_score()
                if self.written_words[self.words_points - 1][number] == \
                        self.set_of_words[self.words_points - 1][number]:
                    self.spelling.append("ok")
                    self.show_correct(self.difference)
                    self.spelling_points = self.count_points()
                    self.mistakes = self.count_mistakes()
                else:
                    self.spelling.append("wrong")
                    self.show_mistake(self.difference)
                    self.spelling_points = self.count_points()
                    self.mistakes = self.count_mistakes()
            else:
                self.show_original_letter()

        except IndexError:
            pass

        # print(self.spelling)
        # print(letters_string)
        # print(self.spelling_points)
        # print(self.words_points)
        # print(self.written_words)

    def count_time(self, count):
        if self.time_start:
            self.time = self.window.after(1000, self.count_time, count + 1)
            self.timer_text['text'] = count

    def start_timer(self):
        if len(self.entry_txt) == 1:
            self.time_start = True
            self.count_time(0)
        elif len(self.entry_txt) == 0:
            self.time_start = False

    def update_screen_board(self):
        self.cpm_value['text'] = self.points
        if int(self.timer_text['text']) > 0:
            self.net_wpm = (int(((self.points / 5) - (self.mistakes * ((int(self.timer_text['text'])) / 60))) /
                                ((int(self.timer_text['text'])) / 60)))
            self.wpm_value['text'] = f"{int((self.points / 5) / ((int(self.timer_text['text'])) / 60))}/" \
                                     f"{self.net_wpm}"
        self.mist_value['text'] = self.mistakes
        if int(self.mist_value['text']) > 0:
            self.mist_value.config(fg="#ff0000")
        elif int(self.mist_value['text']) == 0:
            self.mist_value.config(fg="#fafafa")

    def count_score(self):
        self.time_start = False
        cpm = int(self.points)
        wpm = int((self.points / 5) / ((int(self.timer_text['text'])) / 60))
        net_wpm = (int(((self.points / 5) - (self.mistakes * ((int(self.timer_text['text'])) / 60))) /
                                ((int(self.timer_text['text'])) / 60)))
        accuracy = (net_wpm * 100) / wpm
        messagebox.showinfo("End", f"Your CPM is {cpm}.\n"
                            f"Your WPM is "
                            f"{wpm},\n"
                            f"Net WPN is {net_wpm}.\n"
                            f"Accuracy was "
                            f"{'%.2f' % accuracy}%.")
        self.save_score(self.net_wpm)

    def save_score(self, net_wpn):
        if self.net_wpm > self.high_score:
            self.high_score = self.net_wpm
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

    def restart(self):
        try:
            self.window.destroy()
            self.window.after_cancel(self.time)
            Screen()
        except ValueError:
            Screen()

    def create_widgets(self):
        # timer
        timer_label = Label(text="TIME:", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        timer_label.grid(column=0, row=1, sticky=E)
        self.timer_text = Label(text="0", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        self.timer_text.grid(column=1, row=1, sticky=W)

        # characters per minute
        cpm_label = Label(text=f"CPM: ", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        cpm_label.grid(column=2, row=1, sticky=E)
        self.cpm_value = Label(text="0", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        self.cpm_value.grid(column=3, row=1, sticky=W)

        # words per minute
        wpm_label = Label(text="WPM/NET WPM: ", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        wpm_label.grid(column=4, row=1, sticky=E)
        self.wpm_value = Label(text="0", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        self.wpm_value.grid(column=5, row=1, sticky=W)

        # mistakes
        mist_label = Label(text="MISTAKES: ", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        mist_label.grid(column=6, row=1, sticky=E)
        self.mist_value = Label(text="0", fg="#fafafa", bg="#000000", font=("Tahoma", 12))
        self.mist_value.grid(column=7, row=1, sticky=W)

        # current highest score
        high_score_label = Label(text=f"HIGH SCORE: {self.high_score} NET WPM.",
                                 fg="#fafafa", bg="#000000", font=("Tahoma", 12, "bold"))
        high_score_label.grid(column=8, row=0)

        # entry field
        entry_label = Label(text="WRITE BELOW:", width=15, bg="#000000", fg="#fafafa", font=("Tahoma", 12, "bold"))
        entry_label.grid(column=0, row=5)
        self.entry = StringVar()
        self.entry.trace_add('write', self.text_callback)
        self.entry_field = Entry(self.window, width=100, textvariable=self.entry, bg="#242424", fg="#fafafa",
                                 font=("Arial", 12, "bold"))
        self.entry_field.grid(column=0, row=6, columnspan=8, pady=15)
        self.entry_field.bind("<BackSpace>", self.backspace)

        # restart button
        restart = Button(text="RESTART", font=("Tahoma", 12, "bold"), bg="#000000", fg="#fafafa",
                         command=self.restart)
        restart.grid(column=8, row=6)
