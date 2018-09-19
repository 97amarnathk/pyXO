from game import Game
from board import Board
from agent import Player

p1 = Player()
p2 = Player()

board = Board(3)
game = Game(board, p1, p2)
game.start(verbose = True)
