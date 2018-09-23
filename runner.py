import numpy as np
import matplotlib.pyplot as plt

from game import Game
from board import Board
from agent import Player, MiniMaxAgent, AlphaBetaMiniMaxAgent, RandomAgent
from MCTS import MCTSAgent
import json

log = {}
agents = {
            'RandomAgent': RandomAgent,
            'MiniMaxAgent': MiniMaxAgent,
            'AlphaBetaMiniMaxAgent': AlphaBetaMiniMaxAgent,
            'MCTSAgent': MCTSAgent
        }

runs = 100

for agent1 in list(agents.keys()):
    log[agent1] = {}
    for agent2 in list(agents.keys()):
        wins = {'agent1': [], 'agent2': [], 'draw': 0}
        print()
        print("-"*(len(agent1+agent2)+4))
        print("{} vs {}".format(agent1, agent2))
        print("-"*(len(agent1+agent2)+4))
        for run in range(runs):
            p1 = agents[agent1]()
            p2 = agents[agent2]()
            board = Board(3)
            game = Game(board, p1, p2)
            winner = game.start(verbose = False)
            if winner == 1:
                wins['agent1'].append(np.sum(wins['agent1'])+1)
            elif winner == -1:
                wins['agent2'].append(np.sum(wins['agent2'])+1)
            else:
                wins['draw'] += 1
        log[agent1][agent2] = wins

with open('./complete_data.json', 'w') as f:
    json.dump(log, f, indent = 4)
# plt.plot(winner['RandomAgent']['RandomAgent'])
