from game import Game
from board import Board
from agent import Player, MiniMaxAgent, AlphaBetaMiniMaxAgent, RandomAgent
from MCTS import MCTSAgent

p1 = MiniMaxAgent()
p2 = AlphaBetaMiniMaxAgent()
p3 = MCTSAgent()
p4 = Player()
p5 = RandomAgent()

board = Board(3)
game = Game(board, p5, p3)
game.start(verbose = True)
