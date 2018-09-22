from game import Game
from board import Board
from agent import Player, MiniMaxAgent, AlphaBetaMiniMaxAgent
from MCTS import MCTSAgent

p1 = MiniMaxAgent()
p2 = AlphaBetaMiniMaxAgent()
p3 = MCTSAgent()
p4 = Player()

board = Board(3)
game = Game(board, p1, p3)
game.start(verbose = False)
