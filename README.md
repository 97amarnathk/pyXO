# pyXO
This is an implementation of the classic 3x3 game of Tic-Tac-Toe and is then generalized to an NxN game for any N. The code implements various algorithms like MiniMax, MiniMax with Aplha-Beta pruning and Monte Carlo Tree Search for the bots to play the game.

## Setup
Clone the repository using:
```
git clone https://github.com/97amarnathk/pyXO.git
```

Packages required for running the program are `sys` and `pygame`. If these modules are not present then install the modules using:
```
pip install sys pygame
```

## Run
To start the game, simply go to the directory in the terminal and run the `main.py` file using `python main.py`. This will open the game of Tic-Tac-Toe where you can play using the mouse. The color of your turn depends on which player number you are: `1` or `-1`. `1` corresponds to Blue and `-1` corresponds to Pink.

There are five kinds of agents that can play the game:
  1. Random Agent (`RandomAgent()`)
  2. User (`Player()`)
  3. MiniMax Agent (`MiniMaxAgent()`)
  4. MiniMax Agent with Alpha-Beta pruning (`AlphaBetaMiniMaxAgent()`)
  5. Monte Carlo Tree Search Agent (`MCTSAgent()`)

To change the type of agent, go to `main.py` and change the type of agent to the required one in the `players` dictionary on line 27 and then run the file.


To change the size of the board to NxN, change the argument passed in the initialization of an object of class `Board` on line 23 of `main.py` to N. For example, to play a game on a 5x5 board, change:
        ```board = Board(3)  to  board = Board(5)```
