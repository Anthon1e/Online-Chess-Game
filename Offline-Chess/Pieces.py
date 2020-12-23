import pygame

black = [pygame.image.load('imgs/Pawn_Black.png'), pygame.image.load('imgs/Knight_Black.png'),
         pygame.image.load('imgs/Bishop_Black.png'), pygame.image.load('imgs/Rook_Black.png'),
         pygame.image.load('imgs/Queen_Black.png'), pygame.image.load('imgs/King_Black.png')]
white = [pygame.image.load('imgs/Pawn_White.png'), pygame.image.load('imgs/Knight_White.png'),
         pygame.image.load('imgs/Bishop_White.png'), pygame.image.load('imgs/Rook_White.png'),
         pygame.image.load('imgs/Queen_White.png'), pygame.image.load('imgs/King_White.png')]
red = pygame.image.load('imgs/reddot.png')

Black = True
White = False


class Pawn(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, win):
        if self.color == Black:
            win.blit(black[0], (self.x, self.y))
        else:
            win.blit(white[0], (self.x, self.y))

    def pos_moves(self, board, a, b, color):
        moves = []
        # Black moves
        if color == Black:
            # forward
            if type(board.square[a][b + 1]) == int:
                moves.append((80 * a, 80 * (b + 1)))
                if b == 1:
                    if type(board.square[a][b + 2]) == int:
                        moves.append((80 * a, 80 * (b + 2)))
            # diagonal
            if a < 7:
                if type(board.square[a + 1][b + 1]) != int and board.square[a + 1][b + 1].color == White:
                    moves.append((80 * (a + 1), 80 * (b + 1)))
            if a > 0:
                if type(board.square[a - 1][b + 1]) != int and board.square[a - 1][b + 1].color == White:
                    moves.append((80 * (a - 1), 80 * (b + 1)))
        # White moves
        if color == White:
            # forward
            if type(board.square[a][b - 1]) == int:
                moves.append((80 * a, 80 * (b - 1)))
                if b == 6:
                    if type(board.square[a][b - 2]) == int:
                        moves.append((80 * a, 80 * (b - 2)))
            # diagonal
            if a < 7:
                if type(board.square[a + 1][b - 1]) != int and board.square[a + 1][b - 1].color == Black:
                    moves.append((80 * (a + 1), 80 * (b - 1)))
            if a > 0:
                if type(board.square[a - 1][b - 1]) != int and board.square[a - 1][b - 1].color == Black:
                    moves.append((80 * (a - 1), 80 * (b - 1)))
        return moves


class Rook(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.hasMovedOnce = False

    def draw(self, win):
        if self.color == Black:
            win.blit(black[3], (self.x, self.y))
        else:
            win.blit(white[3], (self.x, self.y))

    def pos_moves(self, board, a, b, color):
        moves = []
        # forward
        for moveCount in range(7):
            if b - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a][b - 1 - moveCount]) == int:
                    moves.append((80 * a, 80 * (b - 1 - moveCount)))
                # enemies' pieces
                elif board.square[a][b - 1 - moveCount].color == (not color):
                    moves.append((80 * a, 80 * (b - 1 - moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        for moveCount in range(7):
            if b + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a][b + 1 + moveCount]) == int:
                    moves.append((80 * a, 80 * (b + 1 + moveCount)))
                # enemies' pieces
                elif board.square[a][b + 1 + moveCount].color == (not color):
                    moves.append((80 * a, 80 * (b + 1 + moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # sideways
        for moveCount in range(7):
            if a - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a - 1 - moveCount][b]) == int:
                    moves.append((80 * (a - 1 - moveCount), 80 * b))
                # enemies' pieces
                elif board.square[a - 1 - moveCount][b].color == (not color):
                    moves.append((80 * (a - 1 - moveCount), 80 * b))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        for moveCount in range(7):
            if a + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a + 1 + moveCount][b]) == int:
                    moves.append((80 * (a + 1 + moveCount), 80 * b))
                # enemies' pieces
                elif board.square[a + 1 + moveCount][b].color == (not color):
                    moves.append((80 * (a + 1 + moveCount), 80 * b))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        return moves


class Knight(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, win):
        if self.color == Black:
            win.blit(black[1], (self.x, self.y))
        else:
            win.blit(white[1], (self.x, self.y))

    def pos_moves(self, board, a, b, color):
        moves = []
        # list of moves
        list = [[a - 1, b - 2], [a - 1, b + 2], [a + 1, b - 2], [a + 1, b + 2], [a + 2, b - 1], [a + 2, b + 1],
                [a - 2, b - 1], [a - 2, b + 1]]
        for countList in range(8):
            if 7 >= list[countList][0] >= 0 and 7 >= list[countList][1] >= 0:
                # blank space
                if type(board.square[list[countList][0]][list[countList][1]]) == int:
                    moves.append((80 * list[countList][0], 80 * list[countList][1]))
                # enemies' pieces
                elif board.square[list[countList][0]][list[countList][1]].color == (not color):
                    moves.append((80 * list[countList][0], 80 * list[countList][1]))
        return moves


class Bishop(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, win):
        if self.color == Black:
            win.blit(black[2], (self.x, self.y))
        else:
            win.blit(white[2], (self.x, self.y))

    def pos_moves(self, board, a, b, color):
        moves = []
        # up left
        for moveCount in range(7):
            if b - 1 - moveCount >= 0 and a - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a - 1 - moveCount][b - 1 - moveCount]) == int:
                    moves.append((80 * (a - 1 - moveCount), 80 * (b - 1 - moveCount)))
                # enemies' pieces
                elif board.square[a - 1 - moveCount][b - 1 - moveCount].color == (not color):
                    moves.append((80 * (a - 1 - moveCount), 80 * (b - 1 - moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # up right
        for moveCount in range(7):
            if b - 1 - moveCount >= 0 and a + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a + 1 + moveCount][b - 1 - moveCount]) == int:
                    moves.append((80 * (a + 1 + moveCount), 80 * (b - 1 - moveCount)))
                # enemies' pieces
                elif board.square[a + 1 + moveCount][b - 1 - moveCount].color == (not color):
                    moves.append((80 * (a + 1 + moveCount), 80 * (b - 1 - moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # down left
        for moveCount in range(7):
            if b + 1 + moveCount <= 7 and a - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a - 1 - moveCount][b + 1 + moveCount]) == int:
                    moves.append((80 * (a - 1 - moveCount), 80 * (b + 1 + moveCount)))
                # enemies' pieces
                elif board.square[a - 1 - moveCount][b + 1 + moveCount].color == (not color):
                    moves.append((80 * (a - 1 - moveCount), 80 * (b + 1 + moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # down right
        for moveCount in range(7):
            if b + 1 + moveCount <= 7 and a + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a + 1 + moveCount][b + 1 + moveCount]) == int:
                    moves.append((80 * (a + 1 + moveCount), 80 * (b + 1 + moveCount)))
                # enemies' pieces
                elif board.square[a + 1 + moveCount][b + 1 + moveCount].color == (not color):
                    moves.append((80 * (a + 1 + moveCount), 80 * (b + 1 + moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        return moves


class Queen(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, win):
        if self.color == Black:
            win.blit(black[4], (self.x, self.y))
        else:
            win.blit(white[4], (self.x, self.y))

    def pos_moves(self, board, a, b, color):
        moves = []
        # forward
        for moveCount in range(7):
            if b - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a][b - 1 - moveCount]) == int:
                    moves.append((80 * a, 80 * (b - 1 - moveCount)))
                # enemies' pieces
                elif board.square[a][b - 1 - moveCount].color == (not color):
                    moves.append((80 * a, 80 * (b - 1 - moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        for moveCount in range(7):
            if b + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a][b + 1 + moveCount]) == int:
                    moves.append((80 * a, 80 * (b + 1 + moveCount)))
                # enemies' pieces
                elif board.square[a][b + 1 + moveCount].color == (not color):
                    moves.append((80 * a, 80 * (b + 1 + moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # sideways
        for moveCount in range(7):
            if a - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a - 1 - moveCount][b]) == int:
                    moves.append((80 * (a - 1 - moveCount), 80 * b))
                # enemies' pieces
                elif board.square[a - 1 - moveCount][b].color == (not color):
                    moves.append((80 * (a - 1 - moveCount), 80 * b))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        for moveCount in range(7):
            if a + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a + 1 + moveCount][b]) == int:
                    moves.append((80 * (a + 1 + moveCount), 80 * b))
                # enemies' pieces
                elif board.square[a + 1 + moveCount][b].color == (not color):
                    moves.append((80 * (a + 1 + moveCount), 80 * b))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # up left
        for moveCount in range(7):
            if b - 1 - moveCount >= 0 and a - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a - 1 - moveCount][b - 1 - moveCount]) == int:
                    moves.append((80 * (a - 1 - moveCount), 80 * (b - 1 - moveCount)))
                # enemies' pieces
                elif board.square[a - 1 - moveCount][b - 1 - moveCount].color == (not color):
                    moves.append((80 * (a - 1 - moveCount), 80 * (b - 1 - moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # up right
        for moveCount in range(7):
            if b - 1 - moveCount >= 0 and a + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a + 1 + moveCount][b - 1 - moveCount]) == int:
                    moves.append((80 * (a + 1 + moveCount), 80 * (b - 1 - moveCount)))
                # enemies' pieces
                elif board.square[a + 1 + moveCount][b - 1 - moveCount].color == (not color):
                    moves.append((80 * (a + 1 + moveCount), 80 * (b - 1 - moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # down left
        for moveCount in range(7):
            if b + 1 + moveCount <= 7 and a - 1 - moveCount >= 0:
                # blank space
                if type(board.square[a - 1 - moveCount][b + 1 + moveCount]) == int:
                    moves.append((80 * (a - 1 - moveCount), 80 * (b + 1 + moveCount)))
                # enemies' pieces
                elif board.square[a - 1 - moveCount][b + 1 + moveCount].color == (not color):
                    moves.append((80 * (a - 1 - moveCount), 80 * (b + 1 + moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        # down right
        for moveCount in range(7):
            if b + 1 + moveCount <= 7 and a + 1 + moveCount <= 7:
                # blank space
                if type(board.square[a + 1 + moveCount][b + 1 + moveCount]) == int:
                    moves.append((80 * (a + 1 + moveCount), 80 * (b + 1 + moveCount)))
                # enemies' pieces
                elif board.square[a + 1 + moveCount][b + 1 + moveCount].color == (not color):
                    moves.append((80 * (a + 1 + moveCount), 80 * (b + 1 + moveCount)))
                    break
                # team's pieces
                else:
                    break
            else:
                break
        return moves


class King(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.hasMovedOnce = False

    def draw(self, win):
        if self.color == Black:
            win.blit(black[5], (self.x, self.y))
        else:
            win.blit(white[5], (self.x, self.y))

    def pos_moves(self, board, a, b, color):
        moves = []
        # list of moves
        list = [[a, b - 1], [a, b + 1], [a + 1, b], [a - 1, b], [a - 1, b - 1], [a - 1, b + 1], [a + 1, b - 1],
                [a + 1, b + 1]]
        for countList in range(8):
            if 7 >= list[countList][0] >= 0 and 7 >= list[countList][1] >= 0:
                # blank space
                if type(board.square[list[countList][0]][list[countList][1]]) == int:
                    moves.append((80 * list[countList][0], 80 * list[countList][1]))
                # enemies' pieces
                elif board.square[list[countList][0]][list[countList][1]].color == (not color):
                    moves.append((80 * list[countList][0], 80 * list[countList][1]))
        # special: castling move
        if not self.hasMovedOnce and board.square[7][b].__class__ == Rook and not board.square[7][b].hasMovedOnce \
                and type(board.square[a + 1][b]) == int \
                and type(board.square[a + 2][b]) == int:
            moves.append((80 * (a + 2), 80 * b))
        if not self.hasMovedOnce and board.square[0][b].__class__ == Rook and not board.square[0][b].hasMovedOnce \
                and type(board.square[a - 1][b]) == int \
                and type(board.square[a - 2][b]) == int \
                and type(board.square[a - 3][b]) == int:
            moves.append((80 * (a - 2), 80 * b))
        return moves
