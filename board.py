import numpy as np

class Board:

    def __init__(self, size):
        self.size = size
        self.state = np.zeros((size, size), dtype = 'int')

    def reset(self):
        self.state.fill(0)

    def __str__(self):
        out = ''
        for i in range(self.size):
            for j in range(self.size):
                char = '_ '
                if self.state[i][j] == 1:
                    char = 'X '
                elif self.state[i][j] == -1:
                    char = 'O '
                out+=char
            out+='\n'
        return out

    def set(self, row, col, currentPlayer):
        self.state[row][col] = currentPlayer

    def check_end(self):
        csum = self.state.sum(axis=0)
        rsum = self.state.sum(axis=1)
        # row or column
        if self.size in csum or self.size in rsum:
            return 1
        elif -1*self.size in csum or -1*self.size in rsum:
            return -1
        # diagonals
        if self.size == self.state.trace() or self.size == np.fliplr(self.state).trace():
            return 1
        elif if -1*self.size == self.state.trace() or -1*self.size == np.fliplr(self.state).trace():
            return -1
        return None
