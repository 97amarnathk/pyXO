import matplotlib.pyplot as plt
import json
import numpy as np

with open('complete_data.json', 'r') as f:
    log = json.load(f)

for i, agent1 in enumerate(list(log.keys())):
    for j, agent2 in enumerate(list(log.keys())):
        plt.plot(np.array(log[agent1][agent2]['agent1'])/(np.arange(len(log[agent1][agent2]['agent1']))+1), label="1. "+agent1)
        plt.plot(np.array(log[agent1][agent2]['agent2'])/(np.arange(len(log[agent1][agent2]['agent2']))+1), label="2. "+agent2)
        plt.plot(np.array(log[agent1][agent2]['draw'])/(np.arange(len(log[agent1][agent2]['draw']))+1), label='draw')
        plt.grid()
        plt.legend()
        plt.ylabel(r"Probability of winning")
        plt.xlabel(r"Games")
        plt.savefig("./plots/prob/{}_{}_{}_{}.png".format(i, j, agent1, agent2), dpi=350)
        plt.close()

for i, agent1 in enumerate(list(log.keys())):
    for j, agent2 in enumerate(list(log.keys())):
        plt.plot(np.array(log[agent1][agent2]['agent1']), label=agent1)
        plt.plot(np.array(log[agent1][agent2]['agent2']), label=agent2)
        plt.plot(np.array(log[agent1][agent2]['draw']), label='draw')
        plt.grid()
        plt.legend()
        plt.ylabel(r"Probability of winning")
        plt.xlabel(r"Games")
        plt.savefig("./plots/runs/{}_{}_{}_{}.png".format(i, j, agent1, agent2), dpi=350)
        plt.close()
