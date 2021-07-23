from copy import deepcopy

import extras


class Piece:
    moves = []

    def __init__(self, name, symbol, team, row, col, points):
        self.name = name
        self.symbol = symbol
        self.team = team
        self.row = row
        self.col = col
        self.points = points
        self.has_moved = False

    def update_indexes(self, r, c):
        self.row = r
        self.col = c

    def get_allowed_moves(self, _board):
        allowed_moves = []

        # go through every move available for this piece
        for move in self.moves:
            row = self.row
            col = self.col

            # potential location to move to
            new_row = row + move[0]
            new_col = col + move[1]

            # check that destination is not out of range
            if _board.in_range(new_row, new_col):
                # check that initial location is not empty
                if not _board.is_cell_empty(row, col):
                    # check that the move is possible for that piece
                    if _board.is_move_possible(self, new_row, new_col):
                        # check that there are no team-mates at destination
                        if not _board.team_at_destination(self, new_row, new_col):
                            # check that there are no team-mates blocking the path
                            if not _board.team_in_path(self, new_row, new_col):
                                # form string representation of the move
                                move = extras.un_parse_input(row, col, new_row, new_col)

                                # add to our list
                                if move not in allowed_moves:
                                    allowed_moves.append(move)

        return allowed_moves

    def get_copy(self):
        copy_ = deepcopy(self)
        copy_.name = deepcopy(self.name)
        copy_.symbol = deepcopy(self.symbol)
        copy_.team = deepcopy(self.team)
        copy_.row = deepcopy(self.row)
        copy_.col = deepcopy(self.col)
        copy_.points = deepcopy(self.points)
        copy_.has_moved = deepcopy(self.has_moved)
        copy_.moves = deepcopy(self.moves)

        return deepcopy(copy_)


class King(Piece):

    def __init__(self, symbol, team, row, col):
        super().__init__('king', symbol, team, row, col, 99999)

        self.moves = [
            [0, 1], [1, 0], [0, -1], [-1, 0],  # right, down, left, up
            [-1, -1], [1, 1], [-1, 1], [-1, -1]  # up-left, down-right, up-right, down-left diagonals
        ]


class Queen(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 9)

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],  # going right
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # going down
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7],  # going left
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0],  # going up
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],  # down-right diagonal
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],  # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7],  # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]  # up-left diagonal


class Rook(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('rook', symbol, team, row, col, 5)

        # (x,y) where x = rows and y = columns

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7],
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]


class Bishop(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('bishop', symbol, team, row, col, 3)

        self.moves = [
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7],
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]


class Knight(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('knight', symbol, team, row, col, 3)

        self.moves = [
            [-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]


class Pawn(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('pawn', symbol, team, row, col, 1)

        self.moves = [
            [-1, 0], [-2, 0], [-1, 1], [-1, -1]]  # Up one cell, Up two cell, Up-right diagonal, Up-left diagonal

    def remove_two_step_move(self):
        if [2, 0] in self.moves:
            self.moves.remove([2, 0])

        if [-2, 0] in self.moves:
            self.moves.remove([-2, 0])
