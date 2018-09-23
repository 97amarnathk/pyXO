class Game:

    def __init__(self, board, playerX, playerO):
        self.board = board
        self.players = {}
        self.players[1] = playerX
        self.players[-1] = playerO

    def start(self, verbose = False):
        # reset the board to empty (0)
        self.board.reset()
        win = None
        if verbose:
            print("New game. {}x{} board.".format(self.board.size, self.board.size))
            print(self.board)

        currentPlayer = 1

        while win is None:
            if verbose:
                print("Player ", currentPlayer)
            perspectiveState = currentPlayer * self.board.state
            row, col = self.players[currentPlayer].turn(perspectiveState)
            self.board.set(row, col, currentPlayer)
            if verbose:
                print(self.board)
            win = self.board.check_end()
            currentPlayer = -1 * currentPlayer

        if win==0:
            print("Draw")
        else:
            print("Player {} wins: {}".format(win, (str(type(self.players[win])).split('.')[-1]).split('Agent')[0]))
        return win
