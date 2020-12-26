import pygame
from network import Network

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


def redrawGameWindow(win, board):
    win.blit(bg, (0, 0))
    board.draw(win)
    for move in board.dots:
        win.blit(red, move)
    pygame.display.update()


# main loop
def main():
    run = True
    # set up the board and hit-box (for clicking)
    # board = Board()
    areas = []
    for y in range(0, 640, 80):
        for x in range(0, 640, 80):
            areas.append(pygame.Rect(x, y, 79, 79))
    clock = pygame.time.Clock()
    # initialize the networking
    n = Network()
    # send the initial object
    p = n.getP()
    redrawGameWindow(win, p)
    while run:
        clock.tick(60)

        if p.playerTurn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button.
                    # Check if the rect collides with the mouse pos.
                    for area in areas:
                        x = round(area.x / 80)
                        y = round(area.y / 80)
                        if area.collidepoint(event.pos):
                            p.move(p, x, y, area, n)
            redrawGameWindow(win, p)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            p = n.send(p)
            while p is None:
                p = n.send(p)

    pygame.quit()

main()