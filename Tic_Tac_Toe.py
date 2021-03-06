import tkinter
from tkinter import *
import pygame
import os

choice1 = ""
choice2 = ""
name1 = ""
name2 = ""
winner = ""
player1_score = 0
player2_score = 0
song = True


def music_path(path):
    path = path + "\\music\\1.mp3"
    return path


def start_music():
    pygame.init()
    current_dir = os.getcwd()
    print(current_dir)
    new_path = music_path(current_dir)
    pygame.mixer.music.load(new_path)
    pygame.mixer.music.play(0)


def stop_music():
    pygame.mixer.music.stop()


class LastWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Tic Tac Toe")
        if winner == "Draw":
            self.text = "Match drawn \n Score Board :"
        else:
            self.text = "Game Over!\n Winner is "+winner+"\n Score Board :"
        self.label1 = tkinter.Label(self, text=self.text, fg='red')
        self.label2 = tkinter.Label(self, text=name1+" = "+str(player1_score))
        self.label3 = tkinter.Label(self, text=name2 + " = "+str(player2_score))
        self.button1 = tkinter.Button(self, text="Continue", command=self.carry_on)
        self.button2 = tkinter.Button(self, text="New Game", command=self.new)
        self.button3 = tkinter.Button(self, text="Main Menu", command=self.main)
        self.label1.grid(row=0, column=0, columnspan=2, rowspan=2)
        self.label2.grid(row=2, column=0, rowspan=2)
        self.label3.grid(row=2, column=1, rowspan=2)
        self.button1.grid(row=4, column=0, columnspan=2)
        self.button2.grid(row=5, column=0, columnspan=2)
        self.button3.grid(row=6, column=0, columnspan=2)

    def carry_on(self):
        self.destroy()
        obj6 = GameWindow()
        obj6.mainloop()

    def new(self):
        self.destroy()
        obj6 = FirstWindow()
        obj6.mainloop()

    def main(self):
        self.destroy()
        obj6 = WelcomeWindow()
        obj6.mainloop()


class GameWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.turn_count = 0
        self.variable = StringVar()
        self.variable = "turn : " + name1
        self.variable1 = StringVar()
        self.variable2 = StringVar()
        self.variable3 = StringVar()
        self.variable4 = StringVar()
        self.variable5 = StringVar()
        self.variable6 = StringVar()
        self.variable7 = StringVar()
        self.variable8 = StringVar()
        self.variable9 = StringVar()
        self.button1 = tkinter.Button(self, width=20, bg='blue', command=self.turn1, fg='black', text="")
        self.button2 = tkinter.Button(self, width=20, bg='blue', command=self.turn2, fg='black', text="")
        self.button3 = tkinter.Button(self, width=20, bg='blue', command=self.turn3, fg='black', text="")
        self.button4 = tkinter.Button(self, width=20, bg='blue', command=self.turn4, fg='black', text="")
        self.button5 = tkinter.Button(self, width=20, bg='blue', command=self.turn5, fg='black', text="")
        self.button6 = tkinter.Button(self, width=20, bg='blue', command=self.turn6, fg='black', text="")
        self.button7 = tkinter.Button(self, width=20, bg='blue', command=self.turn7, fg='black', text="")
        self.button8 = tkinter.Button(self, width=20, bg='blue', command=self.turn8, fg='black', text="")
        self.button9 = tkinter.Button(self, width=20, bg='blue', command=self.turn9, fg='black', text="")
        self.music_button = tkinter.Button(self, text="Stop music", width=20, bg='red', command=self.music,
                                           fg='black')
        self.new_button = tkinter.Button(self, text="New Game", width=20, bg='red', command=self.prev, fg='black')
        self.label = tkinter.Label(self, text="turn : "+name1, width=20)
        self.music_button.grid(row=0, column=0)
        self.label.grid(row=0, column=1)
        self.new_button.grid(row=0, column=2)
        self.button1.grid(row=1, column=0)
        self.button2.grid(row=1, column=1)
        self.button3.grid(row=1, column=2)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button7.grid(row=3, column=0)
        self.button8.grid(row=3, column=1)
        self.button9.grid(row=3, column=2)

    def turn1(self):
        global name1, name2, choice1, choice2
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button1.config(text=choice1)
            self.button1["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable1 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button1.config(text=choice2)
            self.button1["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable1 = choice2
            self.turn_count += 1
            self.win_check()

    def turn2(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button2.config(text=choice1)
            self.button2["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable2 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button2.config(text=choice2)
            self.button2["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable2 = choice2
            self.turn_count += 1
            self.win_check()

    def turn3(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button3.config(text=choice1)
            self.button3["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable3 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button3.config(text=choice2)
            self.button3["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable3 = choice2
            self.turn_count += 1
            self.win_check()

    def turn4(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button4.config(text=choice1)
            self.button4["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable4 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button4.config(text=choice2)
            self.button4["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable4 = choice2
            self.turn_count += 1
            self.win_check()

    def turn5(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button5.config(text=choice1)
            self.button5["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable5 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button5.config(text=choice2)
            self.button5["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable5 = choice2
            self.turn_count += 1
            self.win_check()

    def turn6(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button6.config(text=choice1)
            self.button6["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable6 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button6.config(text=choice2)
            self.button6["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable6 = choice2
            self.turn_count += 1
            self.win_check()

    def turn7(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button7.config(text=choice1)
            self.button7["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable7 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button7.config(text=choice2)
            self.button7["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable7 = choice2
            self.turn_count += 1
            self.win_check()

    def turn8(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button8.config(text=choice1)
            self.button8["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable8 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button8.config(text=choice2)
            self.button8["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable8 = choice2
            self.turn_count += 1
            self.win_check()

    def turn9(self):
        if self.variable == "turn : " + name1:
            self.variable = "turn : " + name2
            self.button9.config(text=choice1)
            self.button9["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable9 = choice1
            self.turn_count += 1
            self.win_check()
        else:
            self.variable = "turn : " + name1
            self.button9.config(text=choice2)
            self.button9["state"] = DISABLED
            self.label.configure(text=self.variable)
            self.variable9 = choice2
            self.turn_count += 1
            self.win_check()

    def prev(self):
        self.destroy()
        obj4 = FirstWindow()
        obj4.mainloop()

    def music(self):
        global song
        if song:
            stop_music()
            self.button3.configure(text="Start music")
            song = False
        else:
            start_music()
            self.button3.configure(text="Stop music")
            song = True

    def win_check(self):
        global name1, name2, choice1, choice2, winner, player1_score, player2_score
        win = False
        if self.variable1 == choice1 and self.variable2 == choice1 and self.variable3 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable4 == choice1 and self.variable5 == choice1 and self.variable6 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable7 == choice1 and self.variable8 == choice1 and self.variable9 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable1 == choice1 and self.variable4 == choice1 and self.variable7 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable2 == choice1 and self.variable5 == choice1 and self.variable8 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable3 == choice1 and self.variable6 == choice1 and self.variable9 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable1 == choice1 and self.variable5 == choice1 and self.variable9 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable3 == choice1 and self.variable5 == choice1 and self.variable7 == choice1:
            win = True
            winner = name1
            player1_score += 1
        elif self.variable1 == choice2 and self.variable2 == choice2 and self.variable3 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.variable4 == choice2 and self.variable5 == choice2 and self.variable6 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.variable7 == choice2 and self.variable8 == choice2 and self.variable9 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.variable1 == choice2 and self.variable4 == choice2 and self.variable7 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.variable2 == choice2 and self.variable5 == choice2 and self.variable8 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.variable3 == choice2 and self.variable6 == choice2 and self.variable9 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.variable1 == choice2 and self.variable5 == choice2 and self.variable9 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.variable3 == choice2 and self.variable5 == choice2 and self.variable7 == choice2:
            win = True
            winner = name2
            player2_score += 1
        elif self.turn_count == 9:
            win = True
            winner = "Draw"

        if win:
            self.destroy()
            obj5 = LastWindow()
            obj5.mainloop()


class FirstWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Tic Tac Toe")
        global player1_score, player2_score
        player1_score = 0
        player2_score = 0
        self.var = StringVar()
        self.values = {"X": "X", "O": "O"}
        self.label1 = tkinter.Label(self, text="Player 1's name")
        self.label2 = tkinter.Label(self, text="Player 2's name")
        self.label3 = tkinter.Label(self, text="Player 1 choose symbol")
        self.entry1 = tkinter.Entry(self)
        self.entry2 = tkinter.Entry(self)
        self.button1 = tkinter.Button(self, text="Enter", command=self.submit1)
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.label3.pack()
        for (self.text, self.value) in self.values.items():
            Radiobutton(self, text=self.text, variable=self.var, value=self.value, command=self.select,
                        tristatevalue="x").pack()
        self.button1.pack()

    def select(self):
        global choice1, choice2
        choice1 = str(self.var.get())
        if choice1 == 'X':
            choice2 = 'O'
        else:
            choice2 = 'X'

    def submit1(self):
        global name1, name2
        name1 = self.entry1.get()
        name2 = self.entry2.get()
        self.destroy()
        obj3 = GameWindow()
        obj3.mainloop()


class WelcomeWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        start_music()
        self.title("Tic Tac Toe")
        self.label = tkinter.Label(self, text="Let's tic tac toe")
        self.button1 = tkinter.Button(self, text="New game", command=self.next)
        self.button2 = tkinter.Button(self, text="Quit", command=self.close)
        self.button3 = tkinter.Button(self, text="Stop music", command=self.music)
        self.label.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def next(self):
        self.destroy()
        obj2 = FirstWindow()
        obj2.mainloop()

    def close(self):
        self.destroy()

    def music(self):
        global song
        if song:
            stop_music()
            self.button3.configure(text="Start music")
            song = False
        else:
            start_music()
            self.button3.configure(text="Stop music")
            song = True


obj = WelcomeWindow()
obj.mainloop()
