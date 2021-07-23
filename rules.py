from colorama import Fore, Back

def rules():
    print(
        Back.CYAN + "                                                                                                      " + Back.RESET)
    print(
        Back.CYAN + "                                             " + Fore.BLACK + "INSTRUCTIONS" + "                                             " + Back.RESET + Fore.RESET)
    print(
        Back.CYAN + "                                                                                                      " + Back.RESET)

    print()
    print(
        Back.CYAN + Fore.BLACK + "1: There are two players: Black & White" + "                                                               " + Back.RESET + Fore.RESET)
    print(
        Back.CYAN + Fore.BLACK + "2: The computer (AI) is given Black color by default meaning you have White pieces." + "                   " + Back.RESET + Fore.RESET)
    print(
        Back.CYAN + Fore.BLACK + "3: The White player will always have the first turn." + "                                                  " + Back.RESET + Fore.RESET)
    print(
        Back.CYAN + Fore.BLACK + "4: In order to move the piece, you will have to type its coordinates in the format (row-column). For  " + Back.RESET + Fore.RESET)
    print(
        Back.CYAN + Fore.BLACK + "   example: if you need to move a piece to '8a', then write it as '8a' (without any space, with       " + Back.RESET + Fore.RESET)
    print(
        Back.CYAN + Fore.BLACK + "   lowercase letter)." + "                                                                                 " + Back.RESET + Fore.RESET)
    print()
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + "                                                " + Fore.BLACK + "RULES" + "                                                 " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print()
    print(
        Back.YELLOW + Fore.BLACK + "1: There are 6 different pieces in chess:" + "                                                             " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + "    " + Fore.BLACK + "a: Rook (worth 5 points)" + "                                                                          " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "    " + Fore.BLACK + "b: Knight (worth 3 points)" + "                                                                        " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "    " + Fore.BLACK + "c: Bishop (worth 3 points)" + "                                                                        " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "    " + Fore.BLACK + "d: Queen (worth 9 points)" + "                                                                         " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "    " + Fore.BLACK + "e: King (worth infinite points)" + "                                                                   " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "    " + Fore.BLACK + "f: Pawn (worth 1 points)" + "                                                                          " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "2: Basic Moves: " + "                                                                                      " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "A: Queen Moves: The Queen can move any number of squares in horizontal, vertical or diagonal " + "         " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   direction as long as the path is not blocked by one of its own pieces." + "                             " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "B: Rook Moves: The Rook can moveee any number of squares horizontally or vertically as long as the " + "   " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   path is not blocked by one of its own pieces." + "                                                      " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "C: Bishop Moves: The Bishop can move any number of squares diagonally as long as the path is not " + "     " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   blocked by one of its own pieces." + "                                                                  " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "D: Knight Moves: The Knight can move in 'L-shape'. It can either move two squares horizontally and one" + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   vertically or two vertically and one horizontally. If its path is blocked by its own teammate, it  " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   can simply jump over it." + "                                                                           " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "E: King Moves: The King can move one square in any direction (horizontal, vertical or diagonal)." + "      " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "F: Pawn Moves: The pawn can move only in forward direction. On the first move it can move two squares" + " " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   at a time while one square at a time on the remaining moves. Furthermore, it cannot attack an" + "      " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "3: Checkmate: Checkmate condition is achieved when King's every possible move is threathened by the " + "  " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   opponent's pieces. This leads to a victory." + "                                                        " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "4: Stalemate: When the King is not in Check but there is no such move which won't lead to the King" + "    " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   being in check. This leads to a draw." + "                                                              " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "5: Illegal Moves: Such moves that lead you king in check. There aren't allowed in our implementation." + " " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + "                                                                                                      " + Back.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "6: Special Move (Castling): Each player can castle only once . In castling, the player moves his King" + " " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   two squares either to its left or right toward one of his Rooks. At the same time, the Rook " + "       " + Back.RESET + Fore.RESET)
    print(
        Back.YELLOW + Fore.BLACK + "   involved goes to the square on the other side of the King." + "                                         " + Back.RESET + Fore.RESET)
    print()
