import ai
import gui
import board
import rules


def game(depth):
    # user's predefined team colour
    player_team = 'white'

    # initialising the AI player
    ai_player = ai.AI('black', depth)

    # initialising the board and its pieces
    chess_board = board.ChessBoard(False)
    chess_board.place_pieces()
    chess_board.update_points()
    chess_board.update_moves()

    chess_board.display()

    while True:
        # take user input
        move_piece = input("\nEnter the piece to move (e.g. 8e):  ")
        move_to = input("Where do you want to move it to: ")

        result, name = chess_board.move_piece(move_piece + move_to, player_team, True)

        if not result:
            print("\nYour move failed. Try again.")

        else:
            print("\nMoving", name, "-", move_piece, "to", move_to)
            chess_board.display()

            # check if user wins
            if board.in_checkmate(chess_board, ai_player.team):
                print("\nAI is in checkmate! You win :)\n")
                break

            if board.in_stalemate(chess_board, ai_player.team):
                print("AI is in stalemate. Game ended in a Draw :/")
                break

            # move by AI
            ai_player.move(chess_board)

            chess_board.display()

            # check if AI wins
            if board.in_checkmate(chess_board, player_team):
                print("You are in checkmate! AI wins hehehe.")
                break

            if board.in_stalemate(chess_board, player_team):
                print("You are in stalemate. Game ended in a Draw :/")
                break


def main():

    choice = input("Press 1 to play in console or 2 to play in GUI: ")

    if choice == '1':
        # display rules
        rules.rules()

        # initialise depth
        depth = -1

        while depth not in [1, 2, 3, 4, 5]:
            depth = int(input("Select a difficulty level (1-5): "))

        # run game
        game(depth)

    elif choice == '2':
        chess_board = board.ChessBoard(False)
        chess_board.place_pieces()
        chess_board.update_points()
        chess_board.update_moves()

        gui.GUI(chess_board)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
