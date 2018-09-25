import sys
import pygame
import colors

from pygame.locals import *

from board import Board
from agent import MiniMaxAgent
from MCTS import MCTSAgent
<<<<<<< Updated upstream

title = 'Tic Tac Toe'

#game config
windowSize = (300, 400)
boardStart = (30, 60)
boardSize = 240
BGCOLOR = colors.WHITE
XCOLOR = colors.CYAN
OCOLOR = colors.PINK
ECOLOR = colors.WHITE
STROKECOLOR = colors.BLACK

board = Board(3)
dim = board.state.shape
blockSize = boardSize/dim[0]

players = {
    1: MiniMaxAgent(),
    0: 'Game Over',
    -1: MCTSAgent()
}

names = {
    1: 'Blue',
    -1: 'Pink',
    0: 'Game Over'
}

def draw_rect(surface, fill_color, outline_color, rect, border=1):
    pygame.draw.rect(surface, fill_color, rect, 0)
    pygame.draw.rect(surface, outline_color, rect, border)

def getBlockColor(x):
    if x==1:
        return XCOLOR
    elif x==-1:
        return OCOLOR
    return ECOLOR

def getBoxAtPixel(x, y):
    for i in range(dim[0]):
        for j in range(dim[1]):
            boxRect = pygame.Rect(boardStart[0] + j*blockSize, boardStart[1] + i*blockSize, blockSize, blockSize)
            if boxRect.collidepoint(x, y):
                return (i, j)
    return (None, None)

#renders the tic tac toe board
def renderBoard(DISPLAYSURF):
    for i in range(dim[0]):
        for j in range(dim[1]):
            blockColor = getBlockColor(board.state[i][j])
            blockStartX = boardStart[0] + j*blockSize
            blockStartY = boardStart[1] + i*blockSize
            rect = pygame.Rect((blockStartX, blockStartY, blockSize, blockSize))
            draw_rect(DISPLAYSURF, blockColor, STROKECOLOR, rect, border=2)

#renders the top text (Game Over, currentPlayer etc)
def renderTextTop(name, myfont, DISPLAYSURF):
    textsurface = myfont.render(name, True, colors.BLACK)
    textWidth = textsurface.get_width()
    textHeight = textsurface.get_height()
    startX = windowSize[0]/2 - textWidth/2
    startY = 15
    DISPLAYSURF.blit(textsurface,(startX, startY))

def renderBottomText(name, myfont, DISPLAYSURF):
    textsurface = myfont.render(name, True, colors.BLACK)
    textWidth = textsurface.get_width()
    textHeight = textsurface.get_height()
    startX = windowSize[0]/2 - textWidth/2
    startY = 330
    DISPLAYSURF.blit(textsurface,(startX, startY))

# initialise game
def init():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(windowSize)
    pygame.display.set_caption(title)
    return DISPLAYSURF

def startGame(DISPLAYSURF, myfont):
    mouseX, mouseY = 0, 0
    currentPlayer = 1
    win = None
    DISPLAYSURF.fill(BGCOLOR)
    renderBoard(DISPLAYSURF)
    renderTextTop(names[currentPlayer], myfont, DISPLAYSURF)
    pygame.display.update()
    #game loop
    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)
        renderBoard(DISPLAYSURF)
        renderTextTop(names[currentPlayer], myfont, DISPLAYSURF)

        #event handlers
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseClicked = True

        #if human player turn
        if players[currentPlayer] == 'Human' and win is None:
            row, col = getBoxAtPixel(mouseX, mouseY)
            if row is not None and col is not None and board.state[row][col]==0:
                blockStartX = boardStart[0] + col*blockSize
                blockStartY = boardStart[1] + row*blockSize
                r = pygame.Rect((blockStartX, blockStartY, blockSize, blockSize))
                draw_rect(DISPLAYSURF, colors.GRAY, STROKECOLOR, r.inflate(5, 5), border=3)
                if mouseClicked:
                    board.state[row][col] = currentPlayer
                    currentPlayer = currentPlayer * -1
                    DISPLAYSURF.fill(BGCOLOR)
                    renderBoard(DISPLAYSURF)
                    renderTextTop(names[currentPlayer], myfont, DISPLAYSURF)

        #if agent turn
        elif win is None:
            pygame.display.update()
            row, col = players[currentPlayer].turn(currentPlayer*board.state)
            board.state[row][col] = currentPlayer
            currentPlayer = currentPlayer * -1
            pygame.font.init()

        if win is None:
            win = board.check_end()
            if win is not None:
                currentPlayer = 0
        else:
            endState = None
            if win==0:
                endState = 'Draw'
            else:
                endState = names[win] + ' WINS!'
            renderBottomText(endState, myfont, DISPLAYSURF)
        pygame.display.update()

def main():
    DISPLAYSURF = init()
    myfont = pygame.font.Font('fonts/font.ttf', 20)
    startGame(DISPLAYSURF, myfont)

if __name__ == '__main__':
    main()

# =======
# import numpy as np
#
# p1 = MiniMaxAgent()
# p2 = AlphaBetaMiniMaxAgent()
# p3 = MCTSAgent()
# p4 = Player()
# p5 = RandomAgent()
#
# board = Board(3)
# game = Game(board, p4, p3)
# game.start(verbose = True)
# # p3.turn(np.array([[0,-1,-1],[0,1,0],[1,0,-1]]))
# # p3.turn(np.array([[0,0,-1],[-1,1,0],[0,-1,1]]))
# # p3.turn(np.array([[-1,-1,0],[-1,1,0],[0,0,1]]))
# # p3.turn(np.array([[0,-1,-1],[0,1,0],[1,0,1]]))
# >>>>>>> Stashed changes
