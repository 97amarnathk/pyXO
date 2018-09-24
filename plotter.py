import matplotlib.pyplot as plt
import json
import numpy as np

with open('complete_data.json', 'r') as f:
    log = json.load(f)

# for i, agent1 in enumerate(list(log.keys())):
#     for j, agent2 in enumerate(list(log.keys())):
#         plt.plot(np.array(log[agent1][agent2]['agent1'])/(np.arange(len(log[agent1][agent2]['agent1']))+1), label="1. "+agent1)
#         plt.plot(np.array(log[agent1][agent2]['agent2'])/(np.arange(len(log[agent1][agent2]['agent2']))+1), label="2. "+agent2)
#         plt.plot(np.array(log[agent1][agent2]['draw'])/(np.arange(len(log[agent1][agent2]['draw']))+1), label='draw')
#         plt.grid()
#         plt.legend()
#         plt.ylabel(r"Ration of outcome (outcome/ total games)")
#         plt.xlabel(r"Games")
#         plt.savefig("./plots/prob/{}_{}_{}_{}.png".format(i, j, agent1, agent2), dpi=350)
#         plt.close()
#
# for i, agent1 in enumerate(list(log.keys())):
#     for j, agent2 in enumerate(list(log.keys())):
#         plt.plot(np.array(log[agent1][agent2]['agent1']), label="1. "+agent1)
#         plt.plot(np.array(log[agent1][agent2]['agent2']), label="2. "+agent2)
#         plt.plot(np.array(log[agent1][agent2]['draw']), label='draw')
#         plt.grid()
#         plt.legend()
#         plt.ylabel(r"Number of outcomes")
#         plt.xlabel(r"Games")
#         plt.savefig("./plots/runs/{}_{}_{}_{}.png".format(i, j, agent1, agent2), dpi=350)
#         plt.close()

# plt.bar(np.arange(len(hist_list)), hist_list, width=0.35, zorder = 3)
# plt.xticks(np.arange(len(hist_names)), hist_names)
# plt.xlabel("Method")
# plt.ylabel("Number of draws")
# plt.title("Number of draws of a method vs MiniMax Agent (First turn of MiniMax)")
# plt.grid()
# plt.savefig("./plots/draw_histogram_minimax_first.png")

''' Stacked bar graph if other method plays first '''

draw_list = np.zeros(len(log))
win_list = np.zeros(len(log))
lose_list = np.zeros(len(log))
hist_names = []
for i, agent in enumerate(list(log.keys())):
    draws = log[agent]['MiniMaxAgent']['draw'][-1]
    lose = log[agent]['MiniMaxAgent']['agent2'][-1]
    win = log[agent]['MiniMaxAgent']['agent1'][-1]
    draw_list[i] = draws
    win_list[i] = win
    lose_list[i] = lose
    hist_names.append(agent.split('Agent')[0])


ind = np.arange(len(hist_names))
width = 0.35
p1 = plt.bar(ind, win_list, width, zorder=2)
p2 = plt.bar(ind, lose_list, width, bottom=win_list, zorder=2)
p3 = plt.bar(ind, draw_list, width, bottom=win_list+lose_list, zorder=2)
plt.xlabel("Method")
plt.grid()
plt.ylabel("Number of draws")
plt.title("Wins, draws and loses vs MiniMax Agent (Second turn of MiniMax)")
plt.xticks(ind, hist_names)
plt.yticks(np.arange(0, 120, 10))
plt.legend((p1[0], p2[0], p3[0]), ('win', 'lose', 'draw'))

for r1, r2, r3 in zip(p1, p2, p3):
    h1 = r1.get_height()
    h2 = r2.get_height()
    h3 = r3.get_height()
    if h1 != 0:
        plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2., "%d" % h1, ha="center", va="center", color="white", fontsize=8, fontweight="bold")
    if h2 != 0:
        plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "%d" % h2, ha="center", va="center", color="white", fontsize=8, fontweight="bold")
    if h3 != 0:
        plt.text(r3.get_x() + r3.get_width() / 2., h1 + h2 + h3/ 3., "%d" % h3, ha="center", va="center", color="white", fontsize=8, fontweight="bold")

plt.savefig("./plots/stackplot_minimax_second.png", dpi=350)
plt.close()

''' Stacked bar graph if MiniMax plays first '''

draw_list = np.zeros(len(log))
win_list = np.zeros(len(log))
lose_list = np.zeros(len(log))
hist_names = []
for i, agent in enumerate(list(log.keys())):
    draws = log['MiniMaxAgent'][agent]['draw'][-1]
    win = log['MiniMaxAgent'][agent]['agent2'][-1]
    lose = log['MiniMaxAgent'][agent]['agent1'][-1]
    draw_list[i] = draws
    win_list[i] = win
    lose_list[i] = lose
    hist_names.append(agent.split('Agent')[0])


ind = np.arange(len(hist_names))
width = 0.35
p1 = plt.bar(ind, win_list, width, zorder=2)
p2 = plt.bar(ind, lose_list, width, bottom=win_list, zorder=2)
p3 = plt.bar(ind, draw_list, width, bottom=win_list+lose_list, zorder=2)
plt.xlabel("Method")
plt.grid()
plt.ylabel("Number of draws")
plt.title("Wins, draws and loses vs MiniMax Agent (First turn of MiniMax)")
plt.xticks(ind, hist_names)
plt.yticks(np.arange(0, 120, 10))
plt.legend((p1[0], p2[0], p3[0]), ('win', 'lose', 'draw'))

for r1, r2, r3 in zip(p1, p2, p3):
    h1 = r1.get_height()
    h2 = r2.get_height()
    h3 = r3.get_height()
    if h1 != 0:
        plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2., "%d" % h1, ha="center", va="center", color="white", fontsize=8, fontweight="bold")
    if h2 != 0:
        plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "%d" % h2, ha="center", va="center", color="white", fontsize=8, fontweight="bold")
    if h3 != 0:
        plt.text(r3.get_x() + r3.get_width() / 2., h1 + h2 + h3/ 3., "%d" % h3, ha="center", va="center", color="white", fontsize=8, fontweight="bold")

plt.savefig("./plots/stackplot_minimax_first.png", dpi=350)
plt.show()
