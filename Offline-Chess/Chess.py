import pygame
from Pieces import Pawn
from Pieces import Rook
from Pieces import Knight
from Pieces import Bishop
from Pieces import Queen
from Pieces import King

pygame.init()

win = pygame.display.set_mode((640, 640))

pygame.display.set_caption("Chess")

black = [pygame.image.load('imgs/Pawn_Black.png'), pygame.image.load('imgs/Knight_Black.png'),
         pygame.image.load('imgs/Bishop_Black.png'), pygame.image.load('imgs/Rook_Black.png'),
         pygame.image.load('imgs/Queen_Black.png'), pygame.image.load('imgs/King_Black.png')]
white = [pygame.image.load('imgs/Pawn_White.png'), pygame.image.load('imgs/Knight_White.png'),
         pygame.image.load('imgs/Bishop_White.png'), pygame.image.load('imgs/Rook_White.png'),
         pygame.image.load('imgs/Queen_White.png'), pygame.image.load('imgs/King_White.png')]
red = pygame.image.load('imgs/reddot.png')
bg = pygame.image.load('imgs/Chess_Board.png')


class Board(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
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


def redrawGameWindow():
    win.blit(bg, (0, 0))
    board.draw(win)
    for move in dots:
        win.blit(red, move)
    # for square in squares:
    #    pygame.draw.rect(win, (255, 0, 0), (square.x, square.y, 79, 79), 2)
    pygame.display.update()


# main loop
Black = True
White = False
board = Board(0, 0)
squares = []
dots = []
areas = []
allowToMove = False
activePlayer = False
for y in range(0, 640, 80):
    for x in range(0, 640, 80):
        areas.append(pygame.Rect(x, y, 79, 79))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button.
            # Check if the rect collides with the mouse pos.
            for area in areas:
                x = round(area.x / 80)
                y = round(area.y / 80)
                if area.collidepoint(event.pos):
                    if allowToMove and len(dots) != 0:
                        for a in dots:
                            # Move is available, append
                            if (area.x, area.y) == a:
                                board.square[x][y] = board.square[saved_x][saved_y]
                                board.square[x][y].x = area.x
                                board.square[x][y].y = area.y
                                board.square[saved_x][saved_y] = 0
                                dots.clear()
                                allowToMove = False
                                # Check castling move
                                if board.square[x][y].__class__ == Rook:
                                    board.square[x][y].hasMovedOnce = True
                                if board.square[x][y].__class__ == King:
                                    board.square[x][y].hasMovedOnce = True
                                    if x == saved_x + 2:
                                        board.square[x - 1][y] = board.square[x + 1][y]
                                        board.square[x - 1][y].x = area.x - 80
                                        board.square[x + 1][y] = 0
                                    if x == saved_x - 2:
                                        board.square[x + 1][y] = board.square[x - 2][y]
                                        board.square[x + 1][y].x = area.x + 80
                                        board.square[x - 2][y] = 0
                                # Change active player
                                if activePlayer:
                                    activePlayer = False
                                else:
                                    activePlayer = True
                                break
                            # Invalid board selection
                            elif type(board.square[x][y]) == int:
                                continue
                            # Choose another pieces, get another list of potential moves
                            if board.square[saved_x][saved_y].color == board.square[x][y].color:
                                dots = board.square[x][y].pos_moves(board, x, y, board.square[x][y].color)
                                saved_x = x
                                saved_y = y
                            # Invalid board selection
                            else:
                                continue
                            allowToMove = True
                    else:
                        # Get a list of potential moves
                        if type(board.square[x][y]) != int and board.square[x][y].color == activePlayer:
                            dots = board.square[x][y].pos_moves(board, x, y, board.square[x][y].color)
                            saved_x = x
                            saved_y = y
                            allowToMove = True

    redrawGameWindow()

pygame.quit()
