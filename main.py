from game import Game
from board import Board
from agent import Player, MiniMaxAgent, AlphaBetaMiniMaxAgent, RandomAgent
from MCTS import MCTSAgent
import numpy as np

p1 = MiniMaxAgent()
p2 = AlphaBetaMiniMaxAgent()
p3 = MCTSAgent()
p4 = Player()
p5 = RandomAgent()

board = Board(4)
game = Game(board, p2, p5)
game.start(verbose = True)
# p3.turn(np.array([[0,-1,-1],[0,1,0],[1,0,-1]]))
# p3.turn(np.array([[0,0,-1],[-1,1,0],[0,-1,1]]))
# p3.turn(np.array([[-1,-1,0],[-1,1,0],[0,0,1]]))
# p3.turn(np.array([[0,-1,-1],[0,1,0],[1,0,1]]))
