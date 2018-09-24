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
        wins = {'agent1': np.zeros(runs), 'agent2': np.zeros(runs), 'draw': np.zeros(runs)}
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
                wins['agent1'][run] = wins['agent1'][run-1]+1
                wins['agent2'][run] = wins['agent2'][run-1]
                wins['draw'][run] = wins['draw'][run-1]
            elif winner == -1:
                wins['agent1'][run] = wins['agent1'][run-1]
                wins['agent2'][run] = wins['agent2'][run-1]+1
                wins['draw'][run] = wins['draw'][run-1]
            else:
                wins['draw'][run] = wins['draw'][run-1] + 1
                wins['agent1'][run] = wins['agent1'][run-1]
                wins['agent2'][run] = wins['agent2'][run-1]

        wins['agent1'] = wins['agent1'].tolist()
        wins['agent2'] = wins['agent2'].tolist()
        wins['draw'] = wins['draw'].tolist()
        log[agent1][agent2] = wins

with open('./complete_data.json', 'w') as f:
    json.dump(log, f, indent = 4)
# plt.plot(winner['RandomAgent']['RandomAgent'])
