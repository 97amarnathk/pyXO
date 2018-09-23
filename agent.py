import numpy as np
import random

class Player:

    def turn(self, perspectiveState):
        r, c = input().split()
        r, c = int(r), int(c)
        return r,c

class MiniMaxAgent:

    def isMovesLeft(self, perspectiveState):
        size = perspectiveState.shape[0]
        #print('!!', np.abs(perspectiveState).sum())
        if np.abs(perspectiveState).sum() == size*size:
            return False
        return True

    def evaluate(self, perspectiveState):
        size = perspectiveState.shape[0]
        rsum = perspectiveState.sum(axis=0)
        csum = perspectiveState.sum(axis=1)
        diagSum = perspectiveState.trace()
        antiDiagSum = np.fliplr(perspectiveState).trace()

        if size in rsum or size in csum or size == diagSum or size == antiDiagSum:
            return 10

        if -1*size in rsum or -1*size in csum or -1*size == diagSum or -1*size == antiDiagSum:
            return -10

        return 0

    def minimax(self, perspectiveState, isMax):
        score = self.evaluate(perspectiveState)

        if score == 10:
            return score

        if score == -10:
            return score

        if not self.isMovesLeft(perspectiveState):
            return 0

        if isMax:
            best = -1000
            for i in range(perspectiveState.shape[0]):
                for j in range(perspectiveState.shape[0]):
                    if perspectiveState[i,j]==0:
                        perspectiveState[i,j] = 1
                        #print('@', isMax)
                        best = max(best, self.minimax(perspectiveState, not isMax))
                        perspectiveState[i,j] = 0
            #print('#', best)
            return best

        else:
            best = 1000;
            for i in range(perspectiveState.shape[0]):
                for j in range(perspectiveState.shape[0]):
                    if perspectiveState[i,j]==0:
                        perspectiveState[i,j] = -1
                        #print('@', isMax)
                        best = min(best, self.minimax(perspectiveState, not isMax))
                        perspectiveState[i,j] = 0
            #print('#', best)
            return best

    def turn(self, perspectiveState):
        r,c = perspectiveState.shape
        bestVal = -1000
        bestR, bestC = -1, -1

        if np.sum(np.abs(perspectiveState)) == 0:
            return 0, 0

        for i in range(r):
            for j in range(c):
                if perspectiveState[i,j] == 0:
                    perspectiveState[i,j] = 1
                    moveVal = self.minimax(perspectiveState, False)
                    #undo
                    perspectiveState[i,j] = 0
                    if moveVal > bestVal:
                        bestVal = moveVal
                        bestR = i
                        bestC = j

        return bestR, bestC

class AlphaBetaMiniMaxAgent:

    def isMovesLeft(self, perspectiveState):
        size = perspectiveState.shape[0]
        #print('!!', np.abs(perspectiveState).sum())
        if np.abs(perspectiveState).sum() == size*size:
            return False
        return True

    def evaluate(self, perspectiveState):
        size = perspectiveState.shape[0]
        rsum = perspectiveState.sum(axis=0)
        csum = perspectiveState.sum(axis=1)
        diagSum = perspectiveState.trace()
        antiDiagSum = np.fliplr(perspectiveState).trace()

        if size in rsum or size in csum or size == diagSum or size == antiDiagSum:
            return 10

        if -1*size in rsum or -1*size in csum or -1*size == diagSum or -1*size == antiDiagSum:
            return -10

        return 0

    def minimax(self, perspectiveState, isMax, alpha, beta):
        score = self.evaluate(perspectiveState)

        if score == 10:
            return score

        if score == -10:
            return score

        if not self.isMovesLeft(perspectiveState):
            return 0

        if isMax:
            best = -100000
            for i in range(perspectiveState.shape[0]):
                for j in range(perspectiveState.shape[0]):
                    if perspectiveState[i,j]==0:
                        perspectiveState[i,j] = 1
                        #print('@', isMax)
                        val = self.minimax(perspectiveState, not isMax, alpha, beta)
                        perspectiveState[i,j] = 0
                        if  val > alpha:
                            alpha = val
                        if alpha >= beta:
                            return beta
            #print('#', best)
            return alpha

        else:
            best = 100000
            for i in range(perspectiveState.shape[0]):
                for j in range(perspectiveState.shape[0]):
                    if perspectiveState[i,j]==0:
                        perspectiveState[i,j] = -1
                        #print('@', isMax)
                        val = self.minimax(perspectiveState, not isMax, alpha, beta)
                        perspectiveState[i,j] = 0
                        if val < beta:
                            beta = val
                        if beta <= alpha:
                            return alpha
            #print('#', best)
            return beta

    def turn(self, perspectiveState):
        r,c = perspectiveState.shape
        bestVal = -1000
        bestR, bestC = -1, -1

        if np.sum(np.abs(perspectiveState)) == 0:
            return 0, 0

        for i in range(r):
            for j in range(c):
                if perspectiveState[i,j] == 0:
                    perspectiveState[i,j] = 1
                    moveVal = self.minimax(perspectiveState, False, -100000, 100000)
                    #undo
                    perspectiveState[i,j] = 0
                    if moveVal > bestVal:
                        bestVal = moveVal
                        bestR = i
                        bestC = j

        return bestR, bestC

class RandomAgent:
    def turn(self, perspectiveState):
        r,c = perspectiveState.shape
        selected = False
        turnR, turnC = None, None
        while not selected:
            turnR = random.randint(0, r-1)
            turnC = random.randint(0, c-1)
            if perspectiveState[turnR, turnC] == 0:
                selected = True

        return turnR, turnC
