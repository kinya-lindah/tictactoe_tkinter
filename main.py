
import tkinter as tk
import tkinter.messagebox as tkmb
import random
from tkinter import *


class Player:  # create class that keeps track on name, letter, and score
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
        self.score = 0


class XOapp:
    def __init__(self, color):
        self.color = color
        self.main_window = tk.Tk()  # only one window
        self.main_window["bg"] = self.color
        self.main_window.title("XO's")
        self.main_window.minsize(500, 650)  # minimum screen size
        self.screen_width = self.main_window.winfo_screenwidth()# next three lines place window at center of page
        self.screen_height = self.main_window.winfo_screenheight()
        x_cordinate = int((self.screen_width / 2) - (500 / 2))
        y_cordinate = int((self.screen_height / 2) - (650 / 2))
        self.main_window.geometry("{}x{}+{}+{}".format(500, 650, x_cordinate, y_cordinate))

        self.frame1 = tk.Frame()
        self.frame2 = tk.Frame()
        self.frame2b = tk.Frame()
        self.frame2a = tk.Frame()
        self.frame3 = tk.Frame()
        self.frame3a = tk.Frame()
        self.p1 = None  # player1
        self.p2 = None  # computer

        self.label1 = tk.Label(self.frame1, text=' ')
        self.label1["bg"] = self.color
        self.label1.pack()
        self.messege1 = tk.Label(self.frame2, text="Hello! Do you want to play xo's with the computer?")
        self.space = tk.Label(self.frame2b, text="")

        self.yes_button = tk.Button(self.frame2a, text="Yes!", highlightbackground=self.color,
                                    command=self.yes)  # the highlightbackground deletes white margin that appears on mac
        self.no_button = tk.Button(self.frame2a, text="No", highlightbackground=self.color, command=self.no)

        #perharps working with images
        self.image1 = PhotoImage(file=r"tictactoe/1_e.png").subsample(2, 2)
        self.image2 = PhotoImage(file=r"tictactoe/2_e.png").subsample(2, 2)
        self.image3 = PhotoImage(file=r"tictactoe/3_e.png").subsample(2, 2)
        self.image4 = PhotoImage(file=r"tictactoe/4_e.png").subsample(2, 2)
        self.image5 = PhotoImage(file=r"tictactoe/5_e.png").subsample(2, 2)
        self.image6 = PhotoImage(file=r"tictactoe/6_e.png").subsample(2, 2)
        self.image7 = PhotoImage(file=r"tictactoe/7_e.png").subsample(2, 2)
        self.image8 = PhotoImage(file=r"tictactoe/8_e.png").subsample(2, 2)
        self.image9 = PhotoImage(file=r"tictactoe/9_e.png").subsample(2, 2)

        self.image1x = PhotoImage(file=r"tictactoe/1_x.png").subsample(2, 2)
        self.image2x = PhotoImage(file=r"tictactoe/2_x.png").subsample(2, 2)
        self.image3x = PhotoImage(file=r"tictactoe/3_x.png").subsample(2, 2)
        self.image4x = PhotoImage(file=r"tictactoe/4_x.png").subsample(2, 2)
        self.image5x = PhotoImage(file=r"tictactoe/5_x.png").subsample(2, 2)
        self.image6x = PhotoImage(file=r"tictactoe/6_x.png").subsample(2, 2)
        self.image7x = PhotoImage(file=r"tictactoe/7_x.png").subsample(2, 2)
        self.image8x = PhotoImage(file=r"tictactoe/8_x.png").subsample(2, 2)
        self.image9x = PhotoImage(file=r"tictactoe/9_x.png").subsample(2, 2)

        self.image1o = PhotoImage(file=r"tictactoe/1_o.png").subsample(2, 2)
        self.image2o = PhotoImage(file=r"tictactoe/2_o.png").subsample(2, 2)
        self.image3o = PhotoImage(file=r"tictactoe/3_o.png").subsample(2, 2)
        self.image4o = PhotoImage(file=r"tictactoe/4_o.png").subsample(2, 2)
        self.image5o = PhotoImage(file=r"tictactoe/5_o.png").subsample(2, 2)
        self.image6o = PhotoImage(file=r"tictactoe/6_o.png").subsample(2, 2)
        self.image7o = PhotoImage(file=r"tictactoe/7_o.png").subsample(2, 2)
        self.image8o = PhotoImage(file=r"tictactoe/8_o.png").subsample(2, 2)
        self.image9o = PhotoImage(file=r"tictactoe/9_o.png").subsample(2, 2)

        self.messege1["bg"] = self.color
        self.space["bg"] = self.color
        self.messege1.pack(side='left')
        self.space.pack()
        self.yes_button.pack(side='left')
        self.no_button.pack(side='left')
        # if no
        self.no_label = tk.Label(self.frame2, text="We are sorry to hear that")
        self.exit = tk.Button(self.frame2b, text="Goodbye", highlightbackground=self.color,
                              command=self.main_window.destroy)
        self.put_info = tk.Button(self.frame2b, text="I actually want to join", highlightbackground=self.color,
                                  command=self.yes)

        # if yes
        self.yes_label = tk.Label(self.frame2, text="Great! Please give us some information !")
        self.player1 = tk.Label(self.frame2b, text="PLAYER 1")
        self.name = tk.Label(self.frame2b, text="Name:    ")
        self.name_input1 = tk.Entry(self.frame2b, width=15)
        self.name_input1["bg"] = self.color

        self.variable = StringVar(self.frame2a)
        self.variable.set("Hard")
        self.difficulty_options = OptionMenu(self.frame2a, self.variable, "Very Easy", "Easy", "Medium", "Hard")
        self.difficulty_options["bg"] = self.color
        self.save_phone_number = tk.Button(self.frame3, text="Start", highlightbackground=self.color, command=self.save)

        self.canvas1 = tk.Button(self.frame2, text="            ", image=self.image1, highlightbackground=self.color,
                                 highlightthickness = 0, command=self.changebutton1, borderwidth=0, bd=0, anchor=E,padx=0,
                                 pady=0, relief=SUNKEN )
        self.canvas2 = tk.Button(self.frame2, text="            ", image=self.image2,highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton2, borderwidth=0, bd=0, anchor=W,padx=0,
                                 pady=0, relief=SUNKEN)
        self.canvas3 = tk.Button(self.frame2, text="            ", image=self.image3, highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton3, borderwidth=0, bd=0, anchor=S,padx=0,
                                 pady=0, relief=SUNKEN )
        self.canvas4 = tk.Button(self.frame2, text="            ", image=self.image4, highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton4, borderwidth=0, bd=0, padx=0, pady=0,
                                 relief=SUNKEN)
        self.canvas5 = tk.Button(self.frame2, text="            ", image=self.image5, highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton5, borderwidth=0, bd=0, anchor=CENTER,
                                 padx=0, pady=0, relief=SUNKEN)
        self.canvas6 = tk.Button(self.frame2, text="            ", image=self.image6, highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton6, borderwidth=0, bd=0, anchor=N,padx=0,
                                 pady=0, relief=SUNKEN)
        self.canvas7 = tk.Button(self.frame2, text="            ", image=self.image7, highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton7, borderwidth=0, bd=0, anchor=W,padx=0,
                                 pady=0, relief=SUNKEN)
        self.canvas8 = tk.Button(self.frame2, text="            ", image=self.image8, highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton8, borderwidth=0, bd=0,padx=0, pady=0, relief=SUNKEN)
        self.canvas9 = tk.Button(self.frame2, text="            ", image=self.image9, highlightbackground=self.color,
                                 highlightthickness=0, command=self.changebutton9, borderwidth=0, bd=0, anchor=E,padx=0,
                                 pady=0, relief=SUNKEN)
        self.restartbutton = tk.Button(self.frame3a, text="Restart", highlightbackground=self.color,
                                       command=self.restart)
        self.availblepoitions = [self.canvas1, self.canvas2, self.canvas3, self.canvas4, self.canvas5, self.canvas6,
                                 self.canvas7, self.canvas8, self.canvas9]
        self.winner = False

        # pack frames
        self.frame1["bg"] = self.color
        self.frame2["bg"] = self.color
        self.frame2b["bg"] = self.color
        self.frame2a["bg"] = self.color
        self.frame3["bg"] = self.color
        self.frame3a["bg"] = self.color
        self.frame1.pack(pady=15)
        self.frame2.pack()
        self.frame2b.pack()
        self.frame2a.pack()
        self.frame3.pack()
        self.frame3a.pack()

        tk.mainloop()

    def yes(self):
        # destory labels and buttons on correct frames and puts correct ones in same frames
        self.messege1.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()
        self.space.destroy()
        self.no_label.destroy()
        self.exit.destroy()
        self.put_info.destroy()
        self.yes_label["bg"] = self.color
        self.player1["bg"] = self.color
        self.name["bg"] = self.color
        self.yes_label.pack()
        self.player1.pack()
        self.name.pack(side='left')
        self.name_input1.pack(side='right')
        self.difficulty_options.pack()
        self.save_phone_number.pack()

    def no(self):
        self.messege1.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()
        self.space.destroy()
        self.no_label["bg"] = self.color
        self.no_label.pack()
        self.exit.pack(side='left')
        self.put_info.pack(side='left')

    def save(self):
        if len(self.name_input1.get()) >= 1:  # save player and computer as 2 players
            self.p1 = Player(self.name_input1.get().capitalize(), "X")
            self.p2 = Player("Computer", "O")
            self.tictactoe()
        else:  # popup saying no name updated
            tkmb.showerror("Failure. Player 1's",
                           f'{self.name_input1.get()} is not a valid valid. please input your name')

    def tictactoe(self):
        self.yes_label.destroy()
        self.player1.destroy()
        self.name.destroy()
        self.name_input1.destroy()
        self.save_phone_number.destroy()

        self.frame2c = tk.Frame()
        self.label2 = tk.Label(self.frame1, text='TicTacToe')
        self.label2["bg"] = self.color
        self.label2.pack()
        self.label3 = tk.Label(self.frame1, text='Press on the position you want to put your X or O on ')
        self.label3["bg"] = self.color
        self.label3.pack()

        self.canvas1.grid(row=1, column=0, sticky="nsew")
        self.canvas2.grid(row=1, column=1, sticky="nsew")
        self.canvas3.grid(row=1, column=2, sticky="nsew")
        self.canvas4.grid(row=2, column=0, sticky="nsew")
        self.canvas5.grid(row=2, column=1, sticky="nsew")
        self.canvas6.grid(row=2, column=2, sticky="nsew")
        self.canvas7.grid(row=3, column=0, sticky="nsew")
        self.canvas8.grid(row=3, column=1, sticky="nsew")
        self.canvas9.grid(row=3, column=2, sticky="nsew")
        self.restartbutton.pack(pady=15)

    # go button by button updating x  when player presses
    def changebutton1(self):
        if self.canvas1['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas1['text'] = "     X     "
            self.canvas1['image'] = self.image1x
            self.availblepoitions.remove(self.canvas1)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:  # if no one won and not draw let computer play
                self.computerplay()

    def changebutton2(self):
        if self.canvas2['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas2['text'] = f"     X     "
            self.canvas2['image'] = self.image2x
            self.availblepoitions.remove(self.canvas2)
            self.win(self.p1)

            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def changebutton3(self):
        if self.canvas3['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas3['text'] = f"     X     "
            self.canvas3['image'] = self.image3x
            self.availblepoitions.remove(self.canvas3)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def changebutton4(self):
        if self.canvas4['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas4['text'] = f"     X     "
            self.canvas4['image'] = self.image4x
            self.availblepoitions.remove(self.canvas4)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def changebutton5(self):
        if self.canvas5['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas5['text'] = f"     X     "
            self.canvas5['image'] = self.image5x
            self.availblepoitions.remove(self.canvas5)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def changebutton6(self):
        if self.canvas6['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas6['text'] = f"     X     "
            self.canvas6['image'] = self.image6x
            self.availblepoitions.remove(self.canvas6)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def changebutton7(self):
        if self.canvas7['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas7['text'] = f"     X     "
            self.canvas7['image'] = self.image7x
            self.availblepoitions.remove(self.canvas7)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def changebutton8(self):
        if self.canvas8['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas8['text'] = f"     X     "
            self.canvas8['image'] = self.image8x
            self.availblepoitions.remove(self.canvas8)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def changebutton9(self):
        if self.canvas9['text'] == "            " and not self.winner and len(self.availblepoitions) > 0:
            self.canvas9['text'] = "     X     "
            self.canvas9['image'] = self.image9x
            self.availblepoitions.remove(self.canvas9)
            self.win(self.p1)
            if not self.winner and len(self.availblepoitions) > 0:
                self.computerplay()

    def computerplay(self):
        winning_positions = [[self.canvas1, self.canvas2, self.canvas3], [self.canvas4, self.canvas5, self.canvas6],
                             [self.canvas7, self.canvas8, self.canvas9],
                             [self.canvas1, self.canvas4, self.canvas7], [self.canvas2, self.canvas5, self.canvas8],
                             [self.canvas3, self.canvas6, self.canvas9],
                             [self.canvas1, self.canvas5, self.canvas9], [self.canvas3, self.canvas5, self.canvas7]]
        computerpick = 0
        # blockplayer1 list will thwart whether player 1 will win after computer plays
        blockplayer1 = []

        # check whether computer can immediately win
        played = False

        if self.variable.get() == "Very Easy":  # if v.easy no checking just random plaecment
            computerpick = random.choice(self.availblepoitions)
            computerpick['text'] = "     O      "
        elif self.variable.get() == "Easy":  # computer only checks where they are going to win
            for i in range(len(winning_positions)):
                check1 = []
                for j in winning_positions[i]:
                    if j['text'] == "     O      ":
                        check1.append(1)
                    elif j['text'] == "     X     ":
                        check1.append(2)
                    else:
                        check1.append(0)
                if check1.count(1) == 2 and check1.count(0) == 1:
                    v = check1.index(0)
                    winning_positions[i][v]['text'] = "     O      "
                    computerpick = winning_positions[i][v]
                    played = True
                    break
            if not played:
                computerpick = random.choice(self.availblepoitions)
                computerpick['text'] = "     O      "
        elif self.variable.get() == 'Medium':
            for i in range(len(winning_positions)):
                check1 = []
                for j in winning_positions[i]:
                    if j['text'] == "     O      ":
                        check1.append(1)
                    elif j['text'] == "     X     ":
                        check1.append(2)
                    else:
                        check1.append(0)
                if check1.count(1) == 2 and check1.count(0) == 1:
                    v = check1.index(0)
                    winning_positions[i][v]['text'] = "     O      "
                    computerpick = winning_positions[i][v]
                    played = True
                    break
                if check1.count(2) == 2 and check1.count(0) == 1:
                    blockplayer1.append([i, check1.index(0)])  # so will be winning_positions[i][check1.index(0)]
            if len(blockplayer1) > 0 and not played:
                pick1 = random.choice(blockplayer1)
                winning_positions[pick1[0]][pick1[1]]['text'] = "     O      "
                computerpick = winning_positions[pick1[0]][pick1[1]]
            elif len(blockplayer1) == 0 and not played:
                computerpick = random.choice(self.availblepoitions)
                computerpick['text'] = "     O      "
        elif self.variable.get() == "Hard":
            setup = []
            for i in range(len(winning_positions)):  # check if comp can win
                check1 = []
                for j in winning_positions[i]:
                    if j['text'] == "     O      ":
                        check1.append(1)
                    elif j['text'] == "     X     ":
                        check1.append(2)
                    else:
                        check1.append(0)
                if check1.count(1) == 2 and check1.count(0) == 1:
                    v = check1.index(0)
                    winning_positions[i][v]['text'] = "     O      "
                    computerpick = winning_positions[i][v]
                    played = True
                    break

                if check1.count(2) == 2 and check1.count(0) == 1:
                    blockplayer1.append([i, check1.index(0)])  # so will be winning_positions[i][check1.index(0)]
                if check1.count(1) == 1 and check1.count(0) == 2:  # setup possibilities
                    p = [winning_positions[i][0], winning_positions[i][1], winning_positions[i][2],
                         winning_positions[i][check1.index(1)]]
                    finalp = []
                    for k in p:
                        if k not in finalp:
                            finalp.append(k)
                        elif k in finalp:
                            finalp.remove(k)
                    setup.append(finalp)

            if len(blockplayer1) > 0 and not played:  # check if player 1 can win
                pick1 = random.choice(blockplayer1)
                winning_positions[pick1[0]][pick1[1]]['text'] = "     O      "
                computerpick = winning_positions[pick1[0]][pick1[1]]
            joints = []
            if len(setup) > 1:
                for i in setup[1]:
                    for j in setup[1]:
                        if j == i:
                            joints.append(j)
            if len(blockplayer1) == 0 and not played and len(joints) > 1:  # check if theres a way to set up a win
                computerpick = random.choice(joints)
                computerpick['text'] = "     O      "
            if len(blockplayer1) == 0 and not played and len(joints) < 2:

                computerpick = random.choice(self.availblepoitions)
                computerpick['text'] = "     O      "

        #change image by first getting which cell the computer picked
        comuputer_images = ['0', self.image1o, self.image2o, self.image3o, self.image4o, self.image5o, self.image6o, self.image7o, self.image8o, self.image9o]
        if str(computerpick)[-1].isdigit():
            computerpick["image"] = comuputer_images[int(str(computerpick)[-1])]
        if str(computerpick)[-1] == "n":
            computerpick["image"] = comuputer_images[1]
        self.win(self.p2)
        self.availblepoitions.remove(computerpick)

    def win(self, player):
        # check horizontal , verticals and diagonals  written as check triple on ps
        if (self.canvas1['text'] == self.canvas2['text'] == self.canvas3['text'] and self.canvas1[
            'text'] != "            ") or (
                self.canvas4['text'] == self.canvas5['text'] == self.canvas6['text'] and self.canvas4[
            'text'] != "            ") or (
                self.canvas7['text'] == self.canvas8['text'] == self.canvas9['text'] and self.canvas7[
            'text'] != "            ") or (
                self.canvas1['text'] == self.canvas4['text'] == self.canvas7['text'] and self.canvas1[
            'text'] != "            ") or (
                self.canvas2['text'] == self.canvas5['text'] == self.canvas8['text'] and self.canvas2[
            'text'] != "            ") or (
                self.canvas3['text'] == self.canvas6['text'] == self.canvas9['text'] and self.canvas3[
            'text'] != "            ") or (
                self.canvas1['text'] == self.canvas5['text'] == self.canvas9['text'] and self.canvas1[
            'text'] != "            ") or (
                self.canvas3['text'] == self.canvas5['text'] == self.canvas7['text'] and self.canvas3[
            'text'] != "            "):
            self.winner = True
            self.win_label = tk.Label(self.frame3a, text=f"{player.name} won")

            self.draw_label = tk.Label(self.frame3a, text="")

            tkmb.showinfo("Winner", f'{player.name} won!!')
            player.score += 1
            self.win_label["bg"] = self.color
            self.draw_label["bg"] = self.color
            self.win_label.pack()
            self.draw_label.pack()
            self.currentscore1 = tk.Label(self.frame3a, text=f"{self.p1.name}'s current score : {self.p1.score}")
            self.currentscore2 = tk.Label(self.frame3a, text=f"{self.p2.name}'s current score : {self.p2.score}")
            self.currentscore1["bg"] = self.color
            self.currentscore2["bg"] = self.color
            self.currentscore1.pack()
            self.currentscore2.pack(pady=10)
        # if draw
        if "            " not in [self.canvas1['text'], self.canvas2['text'], self.canvas3['text'],
                                  self.canvas4['text'], self.canvas5['text'], self.canvas6['text'],
                                  self.canvas7['text'], self.canvas8['text'], self.canvas9['text']] and not self.winner:
            tkmb.showinfo("Draw", 'It was a draw', icon='info')

            self.draw_label = tk.Label(self.frame3a, text="Its a draw!")
            self.win_label = tk.Label(self.frame3a, text=f"")
            self.win_label["bg"] = self.color
            self.draw_label["bg"] = self.color
            self.win_label.pack()
            self.draw_label.pack()
            self.currentscore1 = tk.Label(self.frame3a, text=f"{self.p1.name}'s current score : {self.p1.score}")
            self.currentscore2 = tk.Label(self.frame3a, text=f"{self.p2.name}'s current score : {self.p2.score}")
            self.currentscore1["bg"] = self.color
            self.currentscore2["bg"] = self.color
            self.currentscore1.pack()
            self.currentscore2.pack()

    def restart(self):
        self.canvas1['text'] = "            "
        self.canvas2['text'] = "            "
        self.canvas3['text'] = "            "
        self.canvas4['text'] = "            "
        self.canvas5['text'] = "            "
        self.canvas6['text'] = "            "
        self.canvas7['text'] = "            "
        self.canvas8['text'] = "            "
        self.canvas9['text'] = "            "
        self.canvas1['image'] = self.image1
        self.canvas2['image'] = self.image2
        self.canvas3['image'] = self.image3
        self.canvas4['image'] = self.image4
        self.canvas5['image'] = self.image5
        self.canvas6['image'] = self.image6
        self.canvas7['image'] = self.image7
        self.canvas8['image'] = self.image8
        self.canvas9['image'] = self.image9

        self.winner = False
        for i in [self.canvas1, self.canvas2, self.canvas3, self.canvas4, self.canvas5, self.canvas6, self.canvas7,
                  self.canvas8, self.canvas9]:
            if i not in self.availblepoitions:
                self.availblepoitions.append(i)
        self.win_label.destroy()
        self.draw_label.destroy()
        self.currentscore1.destroy()
        self.currentscore2.destroy()


r4 = XOapp('#f9f9f9')






