from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.ttk as ttk
import random

BACKGROUND = '#EB8F8F'
FOREGROUND = '#F1F3DE'
FONT_NAME = "Courier"
RED = '#CD0A0A'

player1_turn = True


class MyButton:
    def __init__(self):
        self.buttons = [Button(self, text="", bg=BACKGROUND, command=lambda c=i: self.change_button(self.buttons[c]),
                               font=(FONT_NAME, 40, 'bold'), highlightthickness=0,
                               height=1, width=2) for i in range(9)]
        self.make_widget()

    def make_widget(self):

        for i in range(3):
            for j in range(3):
                self.buttons[3 * i + j].grid(row=i, column=6 + j)

    def check_board_for_winner(self):
        message='win'
        # first row
        if (self.buttons[0]['text'] == self.buttons[1]['text'] and self.buttons[1]['text'] ==
                self.buttons[2]['text'] and self.buttons[0]['text'] in ['❌', '⭕']):
            return message

        # second row
        if (self.buttons[3]['text'] == self.buttons[4]['text'] and self.buttons[4]['text'] ==
                self.buttons[5]['text'] and self.buttons[3]['text'] in ['❌', '⭕']):
            return message

        # third row
        if (self.buttons[6]['text'] == self.buttons[7]['text'] and self.buttons[7]['text'] ==
                self.buttons[8]['text'] and self.buttons[6]['text'] in ['❌', '⭕']):
            return message

        # first col
        if (self.buttons[0]['text'] == self.buttons[3]['text'] and self.buttons[3]['text'] ==
                self.buttons[6]['text'] and self.buttons[0]['text'] in ['❌', '⭕']):
            return message

        # second col
        if (self.buttons[1]['text'] == self.buttons[4]['text'] and self.buttons[4]['text'] ==
                self.buttons[7]['text'] and self.buttons[1]['text'] in ['❌', '⭕']):
            return message

        # third col
        if (self.buttons[2]['text'] == self.buttons[5]['text'] and self.buttons[5]['text'] ==
                self.buttons[8]['text'] and self.buttons[2]['text'] in ['❌', '⭕']):
            return message
        # diagonal
        if (self.buttons[0]['text'] == self.buttons[4]['text'] and self.buttons[4]['text'] ==
                self.buttons[8]['text'] and self.buttons[0]['text'] in ['❌', '⭕']):
            return message
        # diagonal
        if (self.buttons[2]['text'] == self.buttons[4]['text'] and self.buttons[4]['text'] ==
                self.buttons[6]['text'] and self.buttons[2]['text'] in ['❌', '⭕']):
            return message
        if (self.buttons[0]['text'] in ['❌', '⭕'] and self.buttons[1]['text']in ['❌', '⭕'] and
                self.buttons[2]['text'] in ['❌', '⭕'] and self.buttons[3]['text']in ['❌', '⭕'] and
                self.buttons[4]['text'] in ['❌', '⭕'] and self.buttons[5]['text']in ['❌', '⭕'] and
                self.buttons[6]['text'] in ['❌', '⭕'] and self.buttons[7]['text']in ['❌', '⭕'] and
                self.buttons[8]['text'] in ['❌', '⭕']):
            return 'tie'
        return 'no decision'

    def reset_board(self):
        for button in self.buttons:
            button['text'] = ''
            button['state'] = NORMAL
            button.configure(bg=BACKGROUND)


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.configure(padx=10, pady=10)

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (Welcome, TwoPlayer, Computer):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')

        self.show_frame(Welcome)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Welcome(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        self.player1 = Entry(self, width=20, font=(FONT_NAME, 12))
        self.label_player1 = Label(self, text='Player1:', font=(FONT_NAME, 15, 'bold'))
        self.label_player1.grid(column=0, row=0, sticky=W)
        # label_player1.config(padx=10)
        self.player1.focus()
        self.player1.insert(END, string='Your Name')
        self.player1.grid(row=1, column=0, sticky=W, pady=10)

        self.player2 = Entry(self, width=20, font=(FONT_NAME, 12))
        self.player2.insert(END, string='Computer')
        self.player2.grid(row=3, column=0, sticky=W, pady=10)
        self.label_player2 = Label(self, text='Player2: (To play against Computer, enter Computer)',
                                   font=(FONT_NAME, 15, 'bold'))
        self.label_player2.grid(column=0, row=2, sticky=W)
        # label_player1.config(padx=10)

        self.cvs = Canvas(self, width=500, height=340)
        welcome_path = "../TicTacToePlay/welcome.webp"
        self.welcome_img = ImageTk.PhotoImage(Image.open(welcome_path))
        self.cvs.create_image(250, 170, image=self.welcome_img)
        self.cvs.grid(row=4, column=0)

        # button to change page

        play_button = Button(self, text="❌ Let's Play ⭕",
                             command=self.change_page,
                             # command=lambda: self.controller.show_frame(TwoPlayer),
                             fg=RED,
                             font=(FONT_NAME, 18, 'bold'), highlightthickness=0)

        play_button.config(pady=10, padx=10)
        play_button.grid(row=5, column=0)

    def change_page(self):

        player2 = self.player2.get()
        if player2 != 'Computer':
            self.controller.show_frame(TwoPlayer)
        else:
            self.controller.show_frame(Computer)


class TwoPlayer(ttk.Frame, MyButton):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.player1_turn = True
        MyButton.__init__(self)

    def change_button(self, button):
        if self.player1_turn:
            button.configure(bg='blue')
            button['text'] = '❌'
        else:
            button.configure(bg='red')
            button['text'] = '⭕'
        button['state'] = DISABLED
        if self.check_board_for_winner() == 'win':

            message = 'Player 1 You Win' if self.player1_turn else 'Player 2 You Win'

            messagebox.askokcancel(title='We have a winner',
                                   message=message)
            # reset board for next time
            self.reset_board()

            self.player1_turn = True
            self.controller.show_frame(Welcome)
        elif self.check_board_for_winner() == 'tie':
            message = "It is a tie"

            messagebox.askokcancel(title='Tic Tac Toe',
                               message=message)
            # reset board for next time
            self.reset_board()

            self.player1_turn = True
            self.controller.show_frame(Welcome)
        else:
            self.player1_turn = not self.player1_turn


class Computer(ttk.Frame, MyButton):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.player1_turn = True
        MyButton.__init__(self)

    # this is only called by player - computer can't click
    def change_button(self, button):

        button.configure(bg='blue')
        button['text'] = '❌'
        if self.check_board_for_winner():
            messagebox.askokcancel(title='We have a winner',
                                   message=' You won')
        else:
            button.configure(bg='red')
            button['text'] = '⭕'
        button['state'] = DISABLED
        self.player1_turn = not self.player1_turn
        if self.is_there_a_winner():
            self.controller.show_frame(Welcome)

    def is_there_a_winner(self):
        i = random.randint(0, 1)
        if i == 1:
            # reset board for next time
            self.reset_board()

            self.player1_turn = True
        return i


if __name__ == '__main__':
    app = MyApp()
    app.title('Tic Tac Toe')
    app.mainloop()
