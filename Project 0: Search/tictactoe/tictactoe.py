"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    cx=0
    co=0
    for i in board:
        for j in i:
            if(j==X):
                cx=cx+1
            elif j==O:
                co=co+1
    if cx>co:
        return O
    else:
        return X
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                s.add((i, j))
    return s

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print(action)
    new_board = [row[:] for row in board] 
    # print(new_board) # Create a new copy of the board
    player_turn = player(board)

    if new_board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid move")

    new_board[action[0]][action[1]] = player_turn
    return new_board

    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    c1=0
    c2=0
    c3=0
    for i in range(len(board)):
        if((board[i][0]==X and board[i][1]==X and board[i][2]==X) or (board[i][0]==O and board[i][1]==O and board[i][2]==O ) ):
            if(board[i][0]==X):
                return X
            else:
                return O
        for j in range(len(board[i])):
            if(board[i][j]==X and j==0):
                c1=c1+1
            elif(board[i][j]==X and j==1):
                c2=c2+1
            elif(board[i][j]==X and j==2):
                c3=c3+1
            elif(board[i][j] and j==0):
                c1=c1-1
            elif(board[i][j]==O and j==1):
                c2=c2-1
            elif(board[i][j]==O and j==2):
                c3=c3-1
    if(c1==3 or c2==3 or c3==3):
        return X
    elif(c1==-3 or c2==-3 or c3==-3):
        return O
    else:
        if(board[1][1]==X and board[2][2]==X and board[0][0]==X):
            return X
        elif board[2][0]==X and board[1][1]==X and board[0][2]==X :
            return X
        elif(board[1][1]==O and board[2][2]==O and board[0][0]==O):
            return O
        elif board[2][0]==O and board[1][1]==O and board[0][2]==O :
            return O
        else:
            return None
        
            




    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2] :
        return True
    elif winner(board)!=None:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    raise NotImplementedError



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        v = float("-inf")
        best_action = None
        for action in actions(board):
            result_value = minval(result(board, action))
            if result_value > v:
                v = result_value
                best_action = action
        return best_action
    else:
        v = float("inf")
        best_action = None
        for action in actions(board):
            result_value = maxval(result(board, action))
            if result_value < v:
                v = result_value
                best_action = action
        return best_action

def maxval(board):
    v = float("-inf")
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minval(result(board, action)))
    return v

def minval(board):
    v = float("inf")
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxval(result(board, action)))
    return v