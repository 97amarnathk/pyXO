from game import Game
from board import Board
from agent import Player, MiniMaxAgent, AlphaBetaMiniMaxAgent

p1 = MiniMaxAgent()
p2 = AlphaBetaMiniMaxAgent()

board = Board(3)
game = Game(board, p1, p2)
game.start(verbose = True)
