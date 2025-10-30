import sys
import math
import random

from typing import Optional


def evaluate(board: list) -> Optional[int]:
    if ((board[0], board[1], board[2]) == (1, 1, 1)
        or (board[3], board[4], board[5]) == (1, 1, 1)
        or (board[6], board[7], board[8]) == (1, 1, 1)
        or (board[0], board[3], board[6]) == (1, 1, 1)
        or (board[1], board[4], board[7]) == (1, 1, 1)
        or (board[2], board[5], board[8]) == (1, 1, 1)
        or (board[0], board[4], board[8]) == (1, 1, 1)
        or (board[2], board[4], board[6]) == (1, 1, 1)):
        return 1
    elif ((board[0], board[1], board[2]) == (2, 2, 2)
          or (board[3], board[4], board[5]) == (2, 2, 2)
          or (board[6], board[7], board[8]) == (2, 2, 2)
          or (board[0], board[3], board[6]) == (2, 2, 2)
          or (board[1], board[4], board[7]) == (2, 2, 2)
          or (board[2], board[5], board[8]) == (2, 2, 2)
          or (board[0], board[4], board[8]) == (2, 2, 2)
          or (board[2], board[4], board[6]) == (2, 2, 2)):
        return -1
    elif min(board):
        return 0
    else:
        return 0.0 # float zero indicates game unfinished

def minimax(board: list, depth: int, player: int):
    evaluation = evaluate(board)
    if depth <= 0 or type(evaluation) != float:
        return evaluation
    elif player == 1: # maximizer
        maximum = -math.inf
        for dex, item in enumerate(board):
            if not item:
                buf = board.copy()
                buf[dex] = 1
                maximum = max(maximum, minimax(buf, depth - 1, 2))
        return maximum
    elif player == 2: # minimizer
        minimum = math.inf
        for dex, item in enumerate(board):
            if not item:
                buf = board.copy()
                buf[dex] = 2
                minimum = min(minimum, minimax(buf, depth - 1, 1))
        return minimum


def main():
    try:
        turn = random.getrandbits(1)
        board = [0] * 9
        difficulty = int(input('Difficulty (0-9): '))
        for i in board:
            if turn: # AI
                minimum = math.inf
                best_moves = []
                for dex, item in enumerate(board):
                    if not item:
                        buf = board.copy()
                        buf[dex] = 2
                        result = minimax(buf, difficulty, 1)
                        if result < minimum:
                            minimum = result
                            best_moves = [dex]
                        elif result == minimum:
                            best_moves.append(dex)
                move = random.choice(best_moves)
                board[move] = 2

                print(board[:3], board[3:6], board[6:], sep='\n')
            else: # HUMAN
                move = int(input('Move (0-8): '))
                while board[move]:
                    move = int(input('Move (0-8): '))
                board[move] = 1
            evaluation = evaluate(board)
            if evaluation == 1:
                print('YOU WIN!')
                break
            elif evaluation == -1:
                print('BOT WINS!')
                break
            elif type(evaluation) != float: # if is float, then still in game
                print('NOBODY WINS!')
            turn = not turn
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()


