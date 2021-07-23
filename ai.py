# This class will contain functionality for computer moves and actions using minimax algorithm
import board
import extras
from copy import deepcopy


class AI:

    def __init__(self, team: str, depth: int):
        self.team = team
        self.depth = depth

    def max_value(self, _board: board.ChessBoard, depth: int, team: str, alpha: int, beta: int) -> (float, str):
        """

        :param _board: object of class ChessBoard (representing a chess board)
        :param depth: depth of minimax tree
        :param team: white or black
        :param alpha: alpha parameter for alpha-beta pruning of minimax algorithm
        :param beta: beta parameter for alpha-beta pruning of minimax algorithm
        :return: returns float value of the board evaluation + string of best move (or None)
        """

        # base condition
        if depth == 0:
            return extras.get_board_evaluation(_board), None

        value = -9999
        best_move = None

        moves = _board.get_all_allowed_moves(team)

        # iterate through all the moves
        for move in moves:
            temp = _board.get_copy()
            temp_board = board.ChessBoard(True)
            temp_board.board = deepcopy(temp)

            # trying the move
            if temp_board.move_piece(move, team, False):
                val, _ = self.min_value(temp_board, depth - 1, extras.get_opposite_team(team), alpha, beta)

                # update best move
                if val > value:
                    value = val
                    best_move = move

                # update alpha
                alpha = max(alpha, value)

                # pruning rather than exploring tree further
                if beta <= alpha:
                    return value, best_move

        return value, best_move

    def min_value(self, _board: board.ChessBoard, depth: int, team: str, alpha: int, beta: int) -> (float, str):
        """

        :param _board: object of class ChessBoard (representing a chess board)
        :param depth: depth of minimax tree
        :param team: white or black
        :param alpha: alpha parameter for alpha-beta pruning of minimax algorithm
        :param beta: beta parameter for alpha-beta pruning of minimax algorithm
        :return: returns float value of the board evaluation + string of best move (or None)
        """

        # base condition
        if depth == 0:
            return extras.get_board_evaluation(_board), None

        value = 9999
        best_move = None

        moves = _board.get_all_allowed_moves(team)

        # iterate through all the moves
        for move in moves:
            temp = _board.get_copy()
            temp_board = board.ChessBoard(True)
            temp_board.board = deepcopy(temp)

            # trying the move
            if temp_board.move_piece(move, team, False):
                val, _ = self.max_value(temp_board, depth - 1, extras.get_opposite_team(team), alpha, beta)

                # update best move
                if val < value:
                    value = val
                    best_move = move

                # update beta
                beta = min(beta, value)

                # pruning rather than exploring tree further
                if beta <= alpha:
                    return value, best_move

        return value, best_move

    def minimax(self, _board: board.ChessBoard) -> str:
        """

        :param _board: object of ChessBoard with the current board configuration
        :return: the best move found (as string)
        """

        alpha = -10000
        beta = 10000

        if self.team == 'black':
            _, best_move = self.min_value(_board, self.depth, 'black', alpha, beta)

        elif self.team == 'white':
            _, best_move = self.max_value(_board, self.depth, 'black', alpha, beta)

        else:
            raise Exception("AI team not defined!")

        return best_move

    def move(self, _board: board.ChessBoard) -> bool:
        """

        :param _board: object of ChessBoard with the current board configuration
        :return: True (if move found and made) otherwise False
        """

        best_move = self.minimax(_board)

        if best_move is not None:
            name = _board.get_piece_name(best_move)
            _board.move_piece(best_move, self.team, False)
            print("\nAI: moving", name, "-", best_move)

            return True

        return False
