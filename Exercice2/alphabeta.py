# /*
#  * /FILE
#  * 	minmax.py
#  * 
#  * /AUTHOR
#  *      REIF Hugo       <hugo.reif.faudemer@gmail.com>  || <21701260@etu.unicaen.fr>
#  *      
#  * /DESCRIPTION 
#  *      Example of minmax algorithm and use on the game of noughts and crosses
#  * 
#  * /DATES
#  *      26/11/2022 : Original Code
#  */
def print_board(state):
    # Print column indices
    print('  0 1 2')
    
    # Print rows with row indices
    for i, row in enumerate(state):
        print(i, row)

class TreeNode:
    def __init__(self, state, parent=None, children=None):
        self.state = state
        self.parent = parent
        if children:
            self.children = children
        else:
            self.children = []

def alphabeta(node, depth, alpha, beta, player):
    # If the depth is 0 or the node has no children (leaf node), return the score of the node
    if depth == 0 or node.children == []:
        return score(node.state)
    
    if player == 'MAX':
        # For each child, find the minimum score of the child's children
        for child in node.children:
            alpha = max(alpha, alphabeta(child, depth-1, alpha, beta, 'MIN'))
            if beta <= alpha:
                break
        return alpha
    else:
        # For each child, find the maximum score of the child's children
        for child in node.children:
            beta = min(beta, alphabeta(child, depth-1, alpha, beta, 'MAX'))
            if beta <= alpha:
                break
        return beta

def score(state):
    # Return 1 if X has won, -1 if O has won, 0 otherwise
    if is_game_won(state, 'X'):
        return 1
    elif is_game_won(state, 'O'):
        return -1
    else:
        return 0

def is_game_won(state, player):
    # Check rows
    for row in state:
        if row == [player, player, player]:
            return True
    
    # Check columns
    for col in range(3):
        if state[0][col] == player and state[1][col] == player and state[2][col] == player:
            return True
            
    # Check diagonals
    if state[0][0] == player and state[1][1] == player and state[2][2] == player:
        return True
    if state[0][2] == player and state[1][1] == player and state[2][0] == player:
        return True
    
    return False
def create_game_tree(state, player, depth):
    # Create a node for the current state
    node = TreeNode(state=state)
    
    # If the depth is 0, return the node
    if depth == 0:
        return node
    
    # Create child nodes for each possible next move
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                # Make a move and create a child node for the resulting state
                new_state = [row[:] for row in state]
                new_state[i][j] = player
                child = create_game_tree(new_state, 'O' if player == 'X' else 'X', depth-1)
                child.parent = node
                node.children.append(child)
    
    return node

def play_game(state, player):
    # Create the game tree
    tree = create_game_tree(state, player, 9)
    
    # Find the best move (the one with the highest score)
    best_move = None
    best_score = float('-inf')
    
    for child in tree.children:
        child_score = alphabeta(child, 9, float('-inf'), float('inf'), 'O')
        if child_score > best_score:
            best_score = child_score
            best_move = child.state
    
    return best_move

# Initial game state
state = [['O', 'X', ' '],
         [' ', 'O', ' '],
         ['O', ' ', 'X']]

print("\n====== Plateau de départ ======")
print_board(state)

# Play game as X
print("\n====== Coup joué grace à l'algorithme alphabeta ======")
print_board(play_game(state, 'X'))
