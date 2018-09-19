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
        print("New game. {}x{} board.".format(self.board.size, self.board.size))
        print(self.board)

        currentPlayer = 1

        while win is None:
            print("Player ", currentPlayer)
            perspectiveState = currentPlayer * self.board.state
            row, col = self.players[currentPlayer].turn(perspectiveState)
            self.board.set(row, col, currentPlayer)
            print(self.board)
            win = self.board.check_end()
            currentPlayer = -1 * currentPlayer

        if win==0:
            print("Draw")
        else:
            print("Player {} wins".format(win))
        return win
