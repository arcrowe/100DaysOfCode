from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.ttk as ttk
import random
import itertools

BACKGROUND = '#EB8F8F'
FOREGROUND = '#F1F3DE'
FONT_NAME = "Courier"
RED = '#CD0A0A'

player1_turn = True


class MyButton:
    def __init__(self):
        self.buttons = [Button(self, text="", bg=BACKGROUND, command=lambda c=i: self.change_button(self.buttons[c]),
                               highlightthickness=0, font=(FONT_NAME, 40, 'bold'),
                               height=1, width=2) for i in range(9)]
        self.make_widget()

    def make_widget(self):

        for i in range(3):
            for j in range(3):
                self.buttons[3 * i + j].grid(row=i, column=6 + j)

    def check_board_for_winner(self):
        message = 'win'
        print(self.buttons[5]['text'])
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
        if (self.buttons[0]['text'] in ['❌', '⭕'] and self.buttons[1]['text'] in ['❌', '⭕'] and
                self.buttons[2]['text'] in ['❌', '⭕'] and self.buttons[3]['text'] in ['❌', '⭕'] and
                self.buttons[4]['text'] in ['❌', '⭕'] and self.buttons[5]['text'] in ['❌', '⭕'] and
                self.buttons[6]['text'] in ['❌', '⭕'] and self.buttons[7]['text'] in ['❌', '⭕'] and
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
        self.cvs = Canvas(self, width=500, height=340)
        welcome_path = "../TicTacToePlay/welcome.webp"
        self.welcome_img = ImageTk.PhotoImage(Image.open(welcome_path))
        self.cvs.create_image(250, 170, image=self.welcome_img)
        self.cvs.grid(row=4, columnspan=2)

        # button to change page

        play_computer = Button(self, text="❌ Computer ⭕",
                               command=lambda: self.controller.show_frame(Computer),
                               fg=RED,
                               font=(FONT_NAME, 18, 'bold'), highlightthickness=0)

        play_computer.config(pady=10, padx=10)
        play_computer.grid(row=5, column=0)

        play_opponent = Button(self, text="❌ Opponent ⭕",
                               command=lambda: self.controller.show_frame(TwoPlayer),
                               fg=RED,
                               font=(FONT_NAME, 18, 'bold'), highlightthickness=0)

        play_opponent.config(pady=10, padx=10)
        play_opponent.grid(row=5, column=1)


class TwoPlayer(ttk.Frame, MyButton):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.player1_turn = True
        MyButton.__init__(self)

        label_player1 = Label(self, text='❌   Player1:', font=(FONT_NAME, 15, 'bold'))
        label_player1.grid(column=0, row=0, sticky=W)
        self.player1 = Entry(self, width=20, font=(FONT_NAME, 12))
        self.player1.focus()
        self.player1.insert(END, string='Your Name')
        self.player1.grid(row=1, column=0, sticky=W, pady=10)

        label_player2 = Label(self, text='⭕   Player2:',
                              font=(FONT_NAME, 15, 'bold'))
        label_player2.grid(column=0, row=2, sticky=W)
        self.player2 = Entry(self, width=20, font=(FONT_NAME, 12))
        self.player2.insert(END, string='The Opponent')
        self.player2.grid(row=3, column=0, sticky=W, pady=10)

    def change_button(self, button):
        if self.player1_turn:
            button.configure(bg='blue')
            button['text'] = '❌'
        else:
            button.configure(bg='red')
            button['text'] = '⭕'
        button['state'] = DISABLED
        if self.check_board_for_winner() == 'win':

            message = f'{self.player1.get()},  You Win' if self.player1_turn else f'{self.player2.get()},  You Win'

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


def check_list(filled, empty):
    spots = {
        'row1': [0, 1, 2],
        'row2': [3, 4, 5],
        'row3': [6, 7, 8],
        'col1': [0, 3, 6],
        'col2': [1, 4, 7],
        'col3': [2, 5, 8],
        'diag1': [0, 4, 8],
        'diag2': [2, 4, 6]
    }
    threats = {
        'row1': [(0, 1), (1, 2), (0, 2)],
        'row2': [(3, 4), (4, 5), (3, 5)],
        'row3': [(6, 7), (7, 8), (6, 8)],
        'col1': [(0, 3), (3, 6), (0, 6)],
        'col2': [(1, 4), (4, 7), (1, 7)],
        'col3': [(2, 5), (5, 8), (2, 8)],
        'diag1': [(0, 4), (4, 8), (0, 8)],
        'diag2': [(2, 4), (4, 6), (2, 6)]
    }

    for j in list(filled):
        for k, v in threats.items():
            if j in v:
                # if threat is determined and available
                if set(spots[k]) & set(empty):
                    return list(set(spots[k]) & set(empty))[0]
                # if threat is determined but already solved - look for more
                else:
                    continue
    # if no threat - pick random spot
    return random.choice(empty)


class Computer(ttk.Frame, MyButton):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.player1_turn = True
        MyButton.__init__(self)

    def change_button(self, button):
        if self.player1_turn:
            button.configure(bg='blue')
            button['text'] = '❌'
            button['state'] = DISABLED
            if self.is_winner('You'):
                self.reset_board()
                self.controller.show_frame(Welcome)
            # computer picks next square
            else:
                self.player1_turn = not self.player1_turn
                i = self.computer_move()
                self.change_button(self.buttons[i])
        # computer has picked next square
        else:
            button.configure(bg='red')
            button['text'] = '⭕'
            button['state'] = DISABLED
            if self.is_winner('Computer'):
                self.reset_board()
                self.controller.show_frame(Welcome)
            else:
                self.player1_turn = not self.player1_turn

    def is_winner(self, winner):
        if self.check_board_for_winner() == 'win':
            messagebox.askokcancel(title='We have a winner',
                                   message=f' {winner} won')
            return True
        elif self.check_board_for_winner() == 'tie':

            messagebox.askokcancel(title='Tic Tac Toe',
                                   message="It is a tie")
            return True
        return False

    def computer_move(self):
        empty_squares = [i for i in range(len(self.buttons)) if self.buttons[i]['text'] == '']
        filled_squares = [i for i in range(len(self.buttons)) if self.buttons[i]['text'] == '❌']

        filled_perm = itertools.permutations(filled_squares, 2)
        spot = check_list(filled_perm, empty_squares)
        return spot


if __name__ == '__main__':
    app = MyApp()
    app.title('Tic Tac Toe')
    app.mainloop()
