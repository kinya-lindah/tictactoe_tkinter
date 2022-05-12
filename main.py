'''import time
import random
import _tkinter as tk
from tkinter.ttk import *
from tkinter import *
from beepy import *
from threading import *


# index
# line 7 simple rockpaperscisors game
# line 78 digital clock with alarm and timer with tkinter gui

# simple rock-paper-scissors game


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


player1 = Player("Player 1")
computer = Player("Computer")


class Game:
    def __init__(self):
        self.winner = False
        self.chosen1 = None
        self.chosen2 = None
        self.docontinue = True
        self.gamenumber = 1

        while not self.winner and self.docontinue:
            print(f'Game number {self.gamenumber}')
            time.sleep(1)
            self.rules()
            time.sleep(1)
            self.playerchoice()

    def winners(self, x, y):  # player 1 rps= x, player 2 rps=y
        if (x == "s" and y == "p") or (x == "r" and y == "s") or (x == "p" and y == "r"):
            self.winner = True
            player1.score += 1
            time.sleep(1)
            print(
                f"\nPlayer 1 wins!\n\nPlayer 1 chose {x} and computer chose {y}. \n\nThe current score is \nPlayer 1: {player1.score} \nComputer: {computer.score}\n")

        elif (y == "s" and x == "p") or (y == "r" and x == "s") or (y == "p" and x == "r"):
            self.winner = True
            computer.score += 1
            time.sleep(1)
            print(
                f"\nComputer wins! \n\nPlayer 1 chose {x} and computer chose {y}.\n\nThe current score is \nPlayer 1: {player1.score} \nComputer: {computer.score}\n")

        else:
            print(
                f"\nIt was a draw\n\nPlayer 1 chose {x} and computer chose {y}.\n\nThe current score is: \nPlayer 1: {player1.score} \nComputer: {computer.score}\n")
        time.sleep(2)
        decision = input("Do you want to continue y/n: ").lower()

        if decision == 'y':
            self.docontinue = True
            self.winner = False
            self.gamenumber += 1
        else:
            self.docontinue = False

    def rules(self):
        print("Paper beats rock, rock beats scissors and scissors beats paper.")

    def playerchoice(self):
        self.chosen1 = input("\nPlease choose r for rock, p for paper and s for scisors: ").lower()
        self.chosen2 = random.choice(['r', 'p', 's'])
        self.winners(self.chosen1, self.chosen2)


# Game()

# digital clock with alarm and timer with tkinter gui

x = 'MidnightBlue'
y = "DarkSlateGray"
timeron = False
alarmon = False
timereached = False
snoozedalarm = False


def pressed():
    if alarmbutton['fg'] == 'black':
        alarmbutton.config(fg='pink')
        alarmlabel.pack(side='left')
        firstpart.pack(side='left')
        secondpart.pack(side='left')
        setbutton2.pack(side='left')
    else:
        variable1.set(timer['text'][:2])
        variable2.set('00')
        global alarmon
        alarmbutton.config(fg="black")
        alarmbutton.config(fg='black')
        setbutton2['fg'] = 'black'
        alarmlabel.pack_forget()
        firstpart.pack_forget()
        secondpart.pack_forget()
        setbutton2.pack_forget()
        if alarmon:
            snoozebutton.pack_forget()
            cancelbutton.pack_forget()
            timer.config(fg=y)
            alarmon = False


def Threaded():
    t = Thread(target=setalarm)
    t.start()


def setalarm():
    global timereached
    global snoozedalarm
    global alarmon
    if setbutton2['fg'] == 'black':
        setbutton2['fg'] = 'pink'
        alarmon = True
        while alarmon:
            set_alarm_time = f"{variable1.get()}:{variable2.get()}"
            time.sleep(2)
            current_time = timer['text'][:5]
            if timer['text'][:5] == set_alarm_time:
                timereached = True
                beep(sound='ping')
                snoozebutton.pack(side=LEFT)
                cancelbutton.pack(side=LEFT)
            if timer['text'][:2] == f'{variable1.get()}' and int(timer['text'][3:5]) == int(variable2.get()) + 1:
                if not snoozedalarm:
                    snoozebutton.pack_forget()
                    cancelbutton.pack_forget()
                    if int(variable2.get()) + 3 > 60:
                        if (int(variable1.get()) + 1) % 24 < 10:
                            variable1.set("0" + str(int(variable1.get() + 1)))
                        elif (int(variable1.get()) + 1) % 24 >= 10:
                            variable1.set(str(int(variable1.get()) + 1))
                        if int(variable2.get()) + 3 - 60 < 10:
                            variable2.set("0" + str(int(variable2.get() + 3 - 60)))
                        elif int(variable2.get()) + 3 - 60 >= 10:
                            variable2.set(str(int(variable2.get() + 3 - 60)))
                    else:
                        variable2.set(str(int(variable2.get()) + 3))
    else:
        setbutton2['fg'] = 'black'
        alarmon = False
        snoozedalarm = False
        if timereached:
            snoozebutton.pack_forget()
            cancelbutton.pack_forget()


def snooze():
    global snoozedalarm
    snoozedalarm = True
    if int(variable2.get()) + 10 > 60:
        print('snoozed')
        if int(variable1.get()) + 1 < 10:
            variable1.set("0" + str(int(variable1.get()) + 1))
        elif int(variable1.get()) + 1 >= 10:
            variable1.set(str(int(variable1.get()) + 1))
        if int(variable2.get()) + 10 - 60 < 10:
            variable2.set("0" + str(int(variable2.get()) + 10 - 60))
        elif int(variable2.get()) + 10 - 60 >= 10:
            variable2.set(str(int(variable2.get()) + 10 - 60))
    else:
        variable2.set(str(int(variable2.get()) + 10))


def cancelalarm():
    global alarmon
    global snoozedalarm
    snoozedalarm = False
    alarmon = False
    snoozebutton.pack_forget()
    cancelbutton.pack_forget()
    setbutton2['fg'] = 'black'
    alarmlabel.pack_forget()
    firstpart.pack_forget()
    secondpart.pack_forget()
    setbutton2.pack_forget()
    alarmbutton.config(fg="black")


def pressedt():
    global timeron
    if timerbutton['fg'] == 'black':
        timerbutton.config(fg="pink")
        timerlabel.pack(side='left')
        thirdpart.pack(side='left')
        forthpart.pack(side='left')
        fifthpart.pack(side='left')
        setbutton.pack(side='left')
        timeron = True
    else:
        timerbutton.config(fg="black")
        setbutton.config(fg="black")
        timerlabel.pack_forget()
        thirdpart.pack_forget()
        forthpart.pack_forget()
        fifthpart.pack_forget()
        setbutton.pack_forget()
        variable5.set('00')
        variable4.set('00')
        variable3.set('00')
        setbutton['text'] = 'START'
        if timeron:
            snoozebuttontimer.pack_forget()
            cancelbuttontimer.pack_forget()
        timeron = False


def settimer():
    global timeron
    if setbutton['fg'] == 'black':
        active()
    elif setbutton['fg'] == 'pink':
        print("THERE")
        variable5.set('00')
        variable4.set('00')
        variable3.set('00')
        setbutton['text'] = 'START'
        timerbutton.config(fg="black")
        setbutton.config(fg="black")
        timerlabel.pack_forget()
        thirdpart.pack_forget()
        forthpart.pack_forget()
        fifthpart.pack_forget()
        setbutton.pack_forget()
        snoozebuttontimer.pack_forget()
        cancelbuttontimer.pack_forget()
        timeron = False


def active():
    global timeron
    snoozebuttontimer.pack(side='left')
    cancelbuttontimer.pack(side='left')
    tt = int(variable3.get()) * 3600 + int(variable4.get()) * 60 + int(variable5.get())
    while tt >= 0 and timeron:
        setbutton['text'] = 'STOP'
        setbutton.config(fg="pink")
        minute, second = (tt // 60, tt % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        variable5.set(second)
        variable4.set(minute)
        variable3.set(hour)
        # Update the time frame
        setframes.update()
        time.sleep(1)
        if (tt == 0):
            variable5.set('00')
            variable4.set('00')
            variable3.set('00')
            beep(sound='ready')
        tt -= 1


def add30():
    tt = int(variable3.get()) * 3600 + int(variable4.get()) * 60 + int(variable5.get())
    tt += 30
    minute, second = (tt // 60, tt % 60)
    hour = 0
    if minute > 60:
        hour, minute = (minute // 60, minute % 60)
    variable5.set(second)
    variable4.set(minute)
    variable3.set(hour)
    active()


def sub30():
    tt = int(variable3.get()) * 3600 + int(variable4.get()) * 60 + int(variable5.get())
    tt -= 30
    minute, second = (tt // 60, tt % 60)
    hour = 0
    if minute > 60:
        hour, minute = (minute // 60, minute % 60)
    variable5.set(second)
    variable4.set(minute)
    variable3.set(hour)
    active()


root = tk.Tk()
root.minsize(500, 350)
root.title("Alarm Clock")
empty = Label(root, text="", bg=x)
empty1 = Label(root, text="", bg=x)

timer = Label(root, text=time.strftime('%H:%M:%S '), font=('calibri', 25, 'bold'), borderwidth=2, relief="raised",
              foreground=y, bg="AliceBlue")
buttonframes = Frame(root)
buttonframes.config(background=x)
alarmbutton = tk.Button(buttonframes, text="Alarm", command=pressed, )
empty2 = Label(buttonframes, text="", bg=x)
timerbutton = Button(buttonframes, text="Timer", command=pressedt)

setframes = Frame(root, bg=x)
empty3 = Label(setframes, text="", bg=x)
variable1 = StringVar(setframes)
variable1.set(timer['text'][:2])
firstpart = OptionMenu(setframes, variable1, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                       '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
variable2 = StringVar(setframes)
variable2.set("00")
secondpart = OptionMenu(setframes, variable2, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                        '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                        '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                        '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                        '60')
setbutton2 = Button(setframes, text="SET", command=Threaded, fg='black')
firstpart.config(bg=x)
secondpart.config(bg=x)

variable3 = StringVar(setframes)
variable3.set("00")
thirdpart = OptionMenu(setframes, variable3, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                       '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
variable4 = StringVar(setframes)
variable4.set("00")
forthpart = OptionMenu(setframes, variable4, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                       '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                       '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                       '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                       '60')
variable5 = StringVar(setframes)
variable5.set("00")
fifthpart = OptionMenu(setframes, variable5, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                       '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                       '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                       '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                       '60')
thirdpart.config(bg=x)
forthpart.config(bg=x)
fifthpart.config(bg=x)
setbutton = Button(setframes, text="START", command=settimer)
alarmlabel = Label(setframes, text="Alarm", bg=x, fg='White')
timerlabel = Label(setframes, text="Timer", bg=x, fg='White')

empty4 = Frame(root, bg=x)
e1 = Label(empty4, bg=x)

snoozeframes = Frame(root, bg=x, bd=6)
snoozebutton = Button(snoozeframes, text="+10 min", borderwidth=0, command=snooze)
cancelbutton = Button(snoozeframes, text="Done", command=cancelalarm)

timersnoozeframes = Frame(root, bg=x)
snoozebuttontimer = Button(timersnoozeframes, text="+30 Seconds", command=add30)
cancelbuttontimer = Button(timersnoozeframes, text="-30 Seconds", command=sub30)
timeleftlabel = Label(timersnoozeframes, text="1", bg=x, relief="raised", fg='white')


def ticker():
    timer.config(text=time.strftime('%H:%M:%S '))
    timer.after(1000, ticker)


empty1.pack()
buttonframes.pack()
alarmbutton.pack(side='left')
empty2.pack(side='left')
timerbutton.pack(side='left')
empty.pack()
timer.pack()
empty3.pack()
setframes.pack()
empty4.pack()
e1.pack()

snoozeframes.pack()
timersnoozeframes.pack()

ticker()
root.config(background=x)
root.mainloop()
'''

'''
# monopoly game without gui
class PlayerMonopoly:
    def __init__(self, name,  pcash, letter):
        self.name = name
        self.pcash = pcash
        self.letter = letter
        self.passets = []


class Monopoly:
    def __init__(self):
        # assets [[property name, if one property, charge this rent]]
        self.assets = [['Mediterranean Ave', 1, -10, 2, -30, 3, -90, 4, -160, 'Shop', -250, 'Mortgage value', -30, 'House cost', -50, 'Shop cost', '50 and 4 houses'], ['Baltic Avenue', 1, -20, 2, -60, 3, -1800, 4, -3200, 'Shop', -450, 'Mortgage value', -30, 'House cost', -50, 'Shop cost', '50 and 4 houses'],
                       ['Oriental Avenue', 1, -30, 2, -90, 3, -270, 4, -400, 'Shop', -550, 'Mortgage value', -50, 'House cost', -50, 'Shop cost', '50 and 4 houses'], ['Vermont Avenue', 1, -30, 2, -90, 3, -270, 4, -400, 'Shop', -550, 'Mortgage value', -50, 'House cost', -50, 'Shop cost', '50 and 4 houses'], ['Vermont Avenue', 1, -40, 2, -100, 3, -300, 4, -450, 'Shop', -600, 'Mortgage value', -60, 'House cost', -50, 'Shop cost', '50 and 4 houses'],
                       ['St Charles Place', 1, -50, 2, -150, 3, -450, 4, -625, 'Shop', -750, 'Mortgage value', -70, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['State Avenue', 1, -50, 2, -150, 3, -450, 4, -625, 'Shop', -750, 'Mortgage value', -70, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['Virginia Avenue', 1, -60, 2, -80, 3, -500, 4, -700, 'Shop', -900, 'Mortgage value', -80, 'House cost', -100, 'Shop cost', '100 and 4 houses'],
                       ['St James Palace', 1, -70, 2, -200, 3, -550, 4, -750, 'Shop', -950, 'Mortgage value', -90, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['Tennessee Avenue', 1, -70, 2, -200, 3, -550, 4, -750, 'Shop', -950, 'Mortgage value', -90, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['New York Avenue', 1, -80, 2, -220, 3, -600, 4, -800, 'Shop', -1000, 'Mortgage value', -100, 'House cost', -110, 'Shop cost', '100 and 4 houses'],
                       ['Kentucky Ave', 1, -90, 2, -250, 3, -700, 4, -875, 'Shop', -1050, 'Mortgage value', -110, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Indiana Avenue', 1, -90, 2, -250, 3, -700, 4, -875, 'Shop', -1050, 'Mortgage value', -110, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Illinois Avenue', 1, -100, 2, -300, 3, -750, 4, -925, 'Shop', -1100, 'Mortgage value', -120, 'House cost', -150, 'Shop cost', '150 and 4 houses'],
                       ['Atlantic Palace', 1, -110, 2, -330, 3, -800, 4, -975, 'Shop', -1150, 'Mortgage value', -130, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Ventor Avenue', 1, -110, 2, -330, 3, -800, 4, -975, 'Shop', -1150, 'Mortgage value', -130, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Marvin Avenue', 1, -120, 2, -360, 3, -850, 4, -1025, 'Shop', -1200, 'Mortgage value', -140, 'House cost', -150, 'Shop cost', '150 and 4 houses'],
                       ['Pacific Ave', 1, -130, 2, -390, 3, -900, 4, -1100, 'Shop', -1275, 'Mortgage value', -150, 'House cost', -200, 'Shop cost', '200 and 4 houses'], ['NC Avenue', 1, -130, 2, -390, 3, -900, 4, -1100, 'Shop', -1275, 'Mortgage value', -150, 'House cost', -200, 'Shop cost', '200 and 4 houses'], ['Pennsylvania Avenue', 1, -150, 2, -450, 3, -1000, 4, -1200, 'Shop', -1400, 'Mortgage value', -160, 'House cost', -200, 'Shop cost', '200 and 4 houses'],
                       ['Park Avenue', 1, -175, 2, -500, 3, -1100, 4, -1300, 'Shop', -1500, 'Mortgage value', -175, 'House cost', -200, 'Shop cost', '200 and 4 houses'], ['Broad Walk', 1, -200, 2, -600, 3, -1400, 4, -1700, 'Shop', -20500, 'Mortgage value', -200, 'House cost', -200, 'Shop cost', '200 and 4 houses'],
                       ['Electric Company', 1, -(self.dice*4), 2, -(self.dice*10)],['Water Works', 1, -(self.dice*4), 2, -(self.dice*10)],
                       ['Reading Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100], ['Pennsylvania Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100], ['B&O Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100], ['Short Line Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100]]
        # board[[spot, (color, property, price), [people on this spot]]
        self.board = [[0, ('none', "GO", 200), []], [1, ('Brown', 'Mediterranean Ave', -60), []],
                      [2, ("none", 'Community chest', 0), []], [3, ('Brown', 'Baltic Avenue', -60), []],
                      [4, ('none', 'Income Tax', -200), []], [5, ('none', 'Reading Railroad', -200), []],
                      [6, ('Blue', 'Oriental Avenue', -100), []], [7, ('none', 'Chance', 0), []],
                      [8, ('Blue', 'Vermont Avenue', -100), []], [9, ('Blue', 'Connecticut Avenue', -120), []],
                      [10, ('none', "In Jail", 0), []], [11, ('Pink', 'St Charles Place', -140), []],
                      [12, ("none", 'Electric Company', 0)], [13, ('Pink', 'State Avenue', -140), []],
                      [14, ('Pink', 'Virginia Avenue', -160), []], [15, ('none', 'Pennsylvania Railroad', -200), []],
                      [16, ('Orange', 'St James Palace', -180), []], [17, ('none', 'Community Chest', 0), []],
                      [18, ('Orange', 'Tennessee Avenue', -180), []], [19, ('Orange', 'New York Avenue', -200), []],
                      [20, ('none', "Free Parking", 0), []], [21, ('Red', 'Kentucky Ave', -220), []],
                      [22, ("none", 'Chance', 0), []], [23, ('Red', 'Indiana Avenue', -220), []],
                      [14, ('Red', 'Illinois Avenue', -240), []], [25, ('none', 'B&O Railroad', -200), []],
                      [26, ('Yellow', 'Atlantic Palace', -260), []], [17, ('Yellow', 'Ventor Avenue', -260), []],
                      [28, ('none', 'Water Works', -150), []], [29, ('Yellow', 'Marvin Avenue', -280), []],
                      [30, ('none', "Go to Jail", 0), []], [31, ('Green', 'Pacific Ave', -300), []],
                      [32, ("Green", 'NC Avenue', -300), []], [33, ("none", 'Community chest', 0), []],
                      [14, ('Green', 'Pennsylvania Avenue', -320), []], [35, ('none', 'Short Line Railroad', -200), []],
                      [36, ("none", 'Chance', 0), []], [37, ('Purple', 'Park Avenue', -350), []],
                      [38, ('none', 'Luxury Tax', -100), []], [29, ('Purple', 'Broad Walk', -400), []]]
        self.cash = 20580

    def roll(self):
        die1 = random.choice([1, 2, 3, 4, 5, 6])
        die2 = random.choice([1, 2, 3, 4, 5, 6])
        self.dice = die1+die2

    def play(self):
        player1name = input("Please type in your name. Player 1: ")
        player2name = input("Please type in your name. Player 2: ")
        player3name = input("Please type in your name. Player 3: ")
        self.p1 = PlayerMonopoly(player1name, 1500, player1name[0].upper())
        self.p2 = PlayerMonopoly(player2name, 1500, player2name[0].upper())
        self.p3 = PlayerMonopoly(player3name, 1500, player3name[0].upper())
        self.continued = True

        while self.p1.pcash + self.p2.pcash + self.p3.pcash == 0 or not self.continued:
            self.cash -= 4500


'''
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






