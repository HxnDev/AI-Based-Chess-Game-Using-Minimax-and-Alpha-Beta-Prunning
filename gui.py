# In order to convert our logic into GUI Interface, we took great help from the below mentioned repository:
# Link: https://github.com/Ugenteraan/Chess-with-Python
# Point to Consider: ONLY SOME GUI FUNCTIONS WERE USED FROM HERE AS WE WERE NEW TO TKINTER

import board
from tkinter import *
import time
import ai

import extras

class GUI:
    mouse_pressed_x = 0
    mouse_pressed_y = 0
    mouse_released_x = 0
    mouse_released_y = 0

    player_team = 'white'
    depth = -1

    # Interface if AI Wins
    def checkmate_black(self):
        cb = Toplevel()
        cb.title("Checkmate Black")
        cb.canvas_width = 800
        cb.canvas_height = 800
        cb = Canvas(cb, bg="Saddle brown", width=cb.canvas_width, height=cb.canvas_height)
        cb.pack()

        cb_img = PhotoImage(file="bg/checkmate.png")

        cb.create_image(-100, 0, anchor=NW, image=cb_img)
        cb.create_text(400, 100, fill='snow', font="Times 30 bold", text="CHECKMATE. AI WON!")
        cb.update()
        cb.mainloop()

    # Interface if Player Wins
    def checkmate_white(self):
        cw = Toplevel()
        cw.title("Checkmate White")
        cw.canvas_width = 800
        cw.canvas_height = 800
        cw = Canvas(cw, bg="Saddle brown", width=cw.canvas_width, height=cw.canvas_height)
        cw.pack()

        cw_img = PhotoImage(file="bg/checkmatew.png")

        cw.create_image(-200, 0, anchor=NW, image=cw_img)
        cw.create_text(400, 100, fill='snow', font="Times 30 bold", text="CHECKMATE. YOU WON!")
        cw.update()
        cw.mainloop()

    def __init__(self, _board):

        def level():
            l = Tk()
            l.title("Select Level (1-3)")
            l1 = Entry(l, width=50)
            l1.pack()
            l1.insert(0, "Select Level (1-3)")

            def on_click():
                self.depth = l1.get()
                self.ai_player.depth = int(self.depth)
                l.destroy()
                play_game()

            my_button = Button(l, text="Select Level", command=on_click)
            my_button.pack()

            l.mainloop()

        def play_game():            # Will store the code to play game
            for i in range(8):
                for j in range(8):
                    if (j + i) % 2 == 0:
                        self.w.create_rectangle(i * self.square_size, j * self.square_size, self.square_size * (i + 1),
                                                self.square_size * (j + 1), fill="saddle brown")
                    else:
                        self.w.create_rectangle(i * self.square_size, j * self.square_size, self.square_size * (i + 1),
                                                self.square_size * (j + 1), fill="lemon chiffon")

            self.root.after(1000, self.draw_board)

        def rules_and_instructions():   # Will store the code to view instructions
            r = Toplevel()
            r.title("Rules and Instructions")
            r.canvas_width = 800
            r.canvas_height = 800
            r1 = Canvas(r, bg="black", width=r.canvas_width, height=r.canvas_height)
            r1.pack()
            r_img = PhotoImage(file="bg/rules.png")
            r1.create_image(-100, 0, anchor=NW, image=r_img)
            r1.create_text(400, 70, fill="snow", font="Times 30 bold", text="Rules And Instructions")
            r1.create_text(80, 120, fill="snow", font="Times 20 bold", text="Instructions:")
            r1.create_text(150, 145, fill="snow", font="Calibri 10 bold", text="1: There are two players: Black & White")
            r1.create_text(269, 160, fill="snow", font="Calibri 10 bold", text="2: The computer (AI) is given Black color by default meaning you have White pieces.")
            r1.create_text(180, 175, fill="snow", font="Calibri 10 bold", text="3: The White player will always have the first turn.")
            r1.create_text(375, 190, fill="snow", font="Calibri 10 bold", text="4: In order to move the piece, you will have to type its coordinates in the format (row-column). For example: if you need ")
            r1.create_text(295, 205, fill="snow", font="Calibri 10 bold",text="to move a piece to '8a', then write it as '8a' (without any space, with lowercase letter).")
            r1.create_text(42, 240, fill="snow", font="Times 20 bold", text="Rules:")
            r1.create_text(150, 265, fill="snow", font="Calibri 10 bold", text="1: There are 6 different pieces in chess:")
            r1.create_text(145, 280, fill="snow", font="Calibri 10 bold", text="a: Rook (worth 5 points)")
            r1.create_text(148, 295, fill="snow", font="Calibri 10 bold", text="b: Knight (worth 3 points)")
            r1.create_text(150, 310, fill="snow", font="Calibri 10 bold", text="c: Bishop (worth 3 points)")
            r1.create_text(150, 325, fill="snow", font="Calibri 10 bold", text="d: Queen (worth 9 points)")
            r1.create_text(158, 340, fill="snow", font="Calibri 10 bold", text="e: King (worth infinite points)")
            r1.create_text(148, 355, fill="snow", font="Calibri 10 bold", text="f: Pawn (worth 1 points)")
            r1.create_text(80, 380, fill="snow", font="Calibri 10 bold", text="2: Basic Moves:")
            r1.create_text(430, 395, fill="snow", font="Calibri 10 bold", text="A: Queen Moves: The Queen can move any number of squares in horizontal, vertical or diagonal direction as long as the path is not ")
            r1.create_text(180, 410, fill="snow", font="Calibri 10 bold", text="blocked by one of its own pieces.")
            r1.create_text(435, 425, fill="snow", font="Calibri 10 bold", text="B: Rook Moves: The Rook can moveee any number of squares horizontally or vertically as long as the path is not blocked by one of its ")
            r1.create_text(120, 440, fill="snow", font="Calibri 10 bold",text="own pieces.")
            r1.create_text(370, 455, fill="snow", font="Calibri 10 bold", text="C: Bishop Moves: The Bishop can move any number of squares diagonally as long as the path is not blocked by ")
            r1.create_text(148, 470, fill="snow", font="Calibri 10 bold",text="one of its own pieces.")
            r1.create_text(425, 485, fill="snow", font="Calibri 10 bold", text="D: Knight Moves: The Knight can move in 'L-shape'. It can either move two squares horizontally and one vertically or two vertically")
            r1.create_text(337, 500, fill="snow", font="Calibri 10 bold",text="and one horizontally. If its path is blocked by its own teammate, it can simply jump over it.")
            r1.create_text(330, 515, fill="snow", font="Calibri 10 bold", text="E: King Moves: The King can move one square in any direction (horizontal, vertical or diagonal).")
            r1.create_text(373, 530, fill="snow", font="Calibri 10 bold", text="F: Pawn Moves: The pawn can move only in forward direction. On the first move it can move two squares at a ")
            r1.create_text(395, 545, fill="snow", font="Calibri 10 bold",text="time while one square at a time on the remaining moves. Furthermore, it cannmot aattack an opponents piece ")
            r1.create_text(340, 560, fill="snow", font="Calibri 10 bold", text="in forward direction. It can only do that in upper diagonals (top-left and top-right) direction.")
            r1.create_text(355, 590, fill="snow", font="Calibri 10 bold", text="3: Checkmate: Checkmate condition is achieved when King's every possible move is threathened by the opponents ")
            r1.create_text(160, 605, fill="snow", font="Calibri 10 bold", text="pieces. This leads to a victory.")
            r1.create_text(352, 630, fill="snow", font="Calibri 10 bold", text="4: Stalemate: When the King is not in Check but there is no such move which won't lead to the King being in check.")
            r1.create_text(135, 645, fill="snow", font="Calibri 10 bold", text=" This leads to a draw.")
            r1.create_text(315, 670, fill="snow", font="Calibri 10 bold", text="5: Illegal Moves: Such moves that lead you king in check. There aren't allowed in our implementation.")
            r1.create_text(383, 695, fill="snow", font="Calibri 10 bold", text="6: Special Move (Castling): Each player can castle only once . In castling, the player moves his King two squares either to its left ")
            r1.create_text(410, 710, fill="snow", font="Calibri 10 bold", text="or right toward one of his Rooks. At the same time, the Rook involved goes to the square on the other side of the King.")
            r1.update()
            r1.mainloop()

        self.chess_board = _board
        self.ai_player = ai.AI('black', self.depth)

        # Main Screen
        self.root = Tk()
        self.root.title("Chess Game")
        self.canvas_width = 800
        self.canvas_height = 800
        self.square_size = 100
        self.w = Canvas(self.root, bg="Saddle brown", width=self.canvas_width, height=self.canvas_height)
        self.w.pack()
        img = PhotoImage(file="bg/bg.png")
        self.w.create_image(-100, 0, anchor=NW, image=img)
        self.w.create_text(400, 100, fill='snow', font="Times 30 bold", text="AI CHESS GAME WITH MINIMAX")
        self.w.update()

        # Adding menu bar to the main screen
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        main_menu = Menu(menubar)
        menubar.add_cascade(label="Main Menu", menu=main_menu)
        main_menu.add_command(label="Play", command=level)
        main_menu.add_separator()
        main_menu.add_command(label="Rules and Instructions", command=rules_and_instructions)
        main_menu.add_separator()
        main_menu.add_command(label="Exit", command=self.root.quit)
        self.root.mainloop()

    # this function fires during a mouse press event
    def mouse_pressed(self, event):
        # get the position of the mouse press and divide with the square size to the get the square of which the
        # mouse pointer is pointed
        self.mouse_pressed_x = int(event.y / self.square_size)
        self.mouse_pressed_y = int(event.x / self.square_size)
        return

    # this function fires when the mouse is released
    def mouse_released(self, event):

        # get the location of the mouse released event
        self.mouse_released_x = event.y
        self.mouse_released_x = int(self.mouse_released_x / self.square_size)
        self.mouse_released_y = event.x
        self.mouse_released_y = int(self.mouse_released_y / self.square_size)

        move = extras.un_parse_input(self.mouse_pressed_x, self.mouse_pressed_y, self.mouse_released_x, self.mouse_released_y)
        result, name = self.chess_board.move_piece(move, 'white', True)

        if not result:
            print("\nYour move failed. Try again.")
        else:
            print("\nMove made by you: ", name, move, "\n")

            if board.in_checkmate(self.chess_board, self.ai_player.team):
                print("\nAI is in checkmate! You win :)\n")
                self.checkmate_white()

            if board.in_stalemate(self.chess_board, self.ai_player.team):
                print("AI is in stalemate. Game ended in a Draw :/")
               

            # move by AI
            self.ai_player.move(self.chess_board)

            # check if AI wins
            if board.in_checkmate(self.chess_board, self.player_team):
                print("You are in checkmate! AI wins.")
                self.checkmate_black()

            if board.in_stalemate(self.chess_board, self.player_team):
                print("You are in stalemate. Game ended in a Draw :/")
            self.root.after(1000, self.draw_board())
        return

    def draw_board(self):
        chess_board = self.chess_board

        self.w.whiteRook = PhotoImage(file='chess_gifs/rookWhite.gif').subsample(4, 4)
        self.w.whiteKnight = PhotoImage(file='chess_gifs/knightWhite.gif').subsample(4, 4)
        self.w.whiteBishop = PhotoImage(file='chess_gifs/bishopWhite.gif').subsample(4, 4)
        self.w.whiteQueen = PhotoImage(file='chess_gifs/queenWhite.gif').subsample(4, 4)
        self.w.whiteKing = PhotoImage(file='chess_gifs/kingWhite.gif').subsample(4, 4)
        self.w.whitePawn = PhotoImage(file='chess_gifs/pawnWhite.gif').subsample(4, 4)

        self.w.blackPawn = PhotoImage(file='chess_gifs/pawnBlack.gif').subsample(4, 4)
        self.w.blackRook = PhotoImage(file='chess_gifs/rookBlack.gif').subsample(4, 4)
        self.w.blackKnight = PhotoImage(file='chess_gifs/knightBlack.gif').subsample(4, 4)
        self.w.blackBishop = PhotoImage(file='chess_gifs/bishopBlack.gif').subsample(4, 4)
        self.w.blackQueen = PhotoImage(file='chess_gifs/queenBlack.gif').subsample(4, 4)
        self.w.blackKing = PhotoImage(file='chess_gifs/kingBlack.gif').subsample(4, 4)

        for i in range(64):
            while chess_board.board[int(i / 8)][i % 8] != ' ':
                if chess_board.board[int(i / 8)][i % 8].symbol == "♖":
                    WRook = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                anchor='nw', image=self.w.whiteRook)
                    self.w.tag_bind(WRook, '<ButtonPress-1>',
                                    self.mouse_pressed)  # binding the rook image with the function Mousepress()
                    self.w.tag_bind(WRook, '<ButtonRelease-1>',
                                    self.mouse_released)  # binding the rook image with the function Mousereleased()

                # if the particular tile on the board has the letter "N", then a white Knight will be placed
                elif chess_board.board[int(i / 8)][i % 8].symbol == "♘":
                    WKnight = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                  anchor='nw', image=self.w.whiteKnight)
                    self.w.tag_bind(WKnight, '<ButtonPress-1>',
                                    self.mouse_pressed)  # binding the knight image with the function Mousepress()
                    self.w.tag_bind(WKnight, '<ButtonRelease-1>',
                                    self.mouse_released)  # binding the knight image with the function Mousereleased()

                # if the particular tile on the board has the letter "B", then a white Bishop will be placed
                elif chess_board.board[int(i / 8)][i % 8].symbol == "♗":
                    WBishop = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                  anchor='nw', image=self.w.whiteBishop)
                    self.w.tag_bind(WBishop, '<ButtonPress-1>',
                                    self.mouse_pressed)  # binding the bishop image with the function Mousepress()
                    self.w.tag_bind(WBishop, '<ButtonRelease-1>',
                                    self.mouse_released)  # binding the bishop image with the function Mousereleased()

                # if the particular tile on the board has the letter "Q", then a white Queen will be placed
                elif chess_board.board[int(i / 8)][i % 8].symbol == "♕":
                    WQueen = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                 anchor='nw', image=self.w.whiteQueen)
                    self.w.tag_bind(WQueen, '<ButtonPress-1>',
                                    self.mouse_pressed)  # binding the queen image with the function Mousepress()
                    self.w.tag_bind(WQueen, '<ButtonRelease-1>',
                                    self.mouse_released)  # binding the queen image with the function Mousereleased()

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♔":
                    WKing = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                anchor='nw', image=self.w.whiteKing)
                    self.w.tag_bind(WKing, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(WKing, '<ButtonRelease-1>', self.mouse_released)

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♙":
                    WPawn = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                anchor='nw', image=self.w.whitePawn)
                    self.w.tag_bind(WPawn, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(WPawn, '<ButtonRelease-1>', self.mouse_released)

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♟":
                    BPawn = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                anchor='nw', image=self.w.blackPawn)
                    self.w.tag_bind(BPawn, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(BPawn, '<ButtonRelease-1>', self.mouse_released)

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♜":
                    BRook = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                anchor='nw', image=self.w.blackRook)
                    self.w.tag_bind(BRook, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(BRook, '<ButtonRelease-1>', self.mouse_released)

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♞":
                    BKnight = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                  anchor='nw', image=self.w.blackKnight)
                    self.w.tag_bind(BKnight, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(BKnight, '<ButtonRelease-1>', self.mouse_released)

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♝":
                    BBishop = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                  anchor='nw', image=self.w.blackBishop)
                    self.w.tag_bind(BBishop, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(BBishop, '<ButtonRelease-1>', self.mouse_released)

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♛":
                    BQueen = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                 anchor='nw', image=self.w.blackQueen)
                    self.w.tag_bind(BQueen, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(BQueen, '<ButtonRelease-1>', self.mouse_released)

                elif chess_board.board[int(i / 8)][i % 8].symbol == "♚":
                    BKing = self.w.create_image((i % 8) * self.square_size + 2, int(i / 8) * self.square_size + 2,
                                                anchor='nw', image=self.w.blackKing)
                    self.w.tag_bind(BKing, '<ButtonPress-1>', self.mouse_pressed)
                    self.w.tag_bind(BKing, '<ButtonRelease-1>', self.mouse_released)
                i += 1
