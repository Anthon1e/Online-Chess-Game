from pieces import Pawn
from pieces import Rook
from pieces import Knight
from pieces import Bishop
from pieces import Queen
from pieces import King

Black = True
White = False


class Board(object):
    def __init__(self, playerTurn):
        self.done = False
        self.playerTurn = playerTurn
        self.dots = []
        self.saved_x = 0
        self.saved_y = 0
        self.allowToMove = False
        self.activePlayer = False
        self.square = [[0 for _ in range(8)] for _ in range(8)]

        self.square[0][0] = Rook(0, 0, Black)
        self.square[1][0] = Knight(80, 0, Black)
        self.square[2][0] = Bishop(160, 0, Black)
        self.square[3][0] = Queen(240, 0, Black)
        self.square[4][0] = King(320, 0, Black)
        self.square[5][0] = Bishop(400, 0, Black)
        self.square[6][0] = Knight(480, 0, Black)
        self.square[7][0] = Rook(560, 0, Black)

        self.square[0][7] = Rook(0, 560, White)
        self.square[1][7] = Knight(80, 560, White)
        self.square[2][7] = Bishop(160, 560, White)
        self.square[3][7] = Queen(240, 560, White)
        self.square[4][7] = King(320, 560, White)
        self.square[5][7] = Bishop(400, 560, White)
        self.square[6][7] = Knight(480, 560, White)
        self.square[7][7] = Rook(560, 560, White)

        for a in range(0, 8):
            self.square[a][1] = Pawn(a*80, 80, Black)

        for a in range(0, 8):
            self.square[a][6] = Pawn(a*80, 480, White)

    def draw(self, win):
        for y in range(0, 8):
            for x in range(0, 8):
                if type(self.square[x][y]) != int:
                    self.square[x][y].draw(win)

    def move(self, board, x, y, area, n):
        # Given permission to move (after selecting the piece)
        if self.allowToMove and len(self.dots) != 0:
            for a in self.dots:
                # Move is available, append
                if (area.x, area.y) == a:
                    self.square[x][y] = self.square[self.saved_x][self.saved_y]
                    self.square[x][y].x = area.x
                    self.square[x][y].y = area.y
                    self.square[self.saved_x][self.saved_y] = 0
                    self.dots.clear()
                    self.allowToMove = False
                    # Check castling move
                    if self.square[x][y].__class__ == Rook:
                        self.square[x][y].hasMovedOnce = True
                    if self.square[x][y].__class__ == King:
                        self.square[x][y].hasMovedOnce = True
                        if x == self.saved_x + 2:   # right side
                            self.square[x - 1][y] = self.square[x + 1][y]
                            self.square[x - 1][y].x = area.x - 80
                            self.square[x + 1][y] = 0
                        if x == self.saved_x - 2:   # left side
                            self.square[x + 1][y] = self.square[x - 2][y]
                            self.square[x + 1][y].x = area.x + 80
                            self.square[x - 2][y] = 0
                    # Change active player
                    if self.activePlayer:
                        self.activePlayer = False
                    else:
                        self.activePlayer = True
                    n.send(board)
                    board.playerTurn = False
                    break
                # Invalid board selection
                elif type(self.square[x][y]) == int:
                    continue
                # Choose another pieces, get another list of potential moves
                if self.square[self.saved_x][self.saved_y].color == self.square[x][y].color:
                    self.dots = self.square[x][y].pos_moves(board, x, y, self.square[x][y].color)
                    self.saved_x = x
                    self.saved_y = y
                # Invalid board selection
                else:
                    continue
                self.allowToMove = True
        # Get a list of potential moves
        else:
            if type(self.square[x][y]) != int and self.square[x][y].color == self.activePlayer:
                self.dots = self.square[x][y].pos_moves(board, x, y, self.square[x][y].color)
                self.saved_x = x
                self.saved_y = y
                self.allowToMove = True