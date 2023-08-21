# Define the goal state
goal_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))

# Define the initial state
initial_state = ((2, 8, 3), (1, 6, 4), (7, 0, 5))

# Define the predefined depth limit
L = 10

# Function to check if a state is the goal state
def is_goal(state):
    return state == goal_state

# Function to find possible actions/moves
def get_possible_actions(state):
    actions = []
    row, col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j
                break

    # Possible moves: Up, Down, Left, Right
    possible_moves = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

    for move in possible_moves:
        if 0 <= move[0] < 3 and 0 <= move[1] < 3:
            actions.append(move)

    return actions

# Function to perform a move on a state
def perform_move(state, move):
    row1, col1 = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row1, col1 = i, j
                break

    row2, col2 = move
    state = list(map(list, state))
    state[row1][col1], state[row2][col2] = state[row2][col2], state[row1][col1]
    return tuple(map(tuple, state))

# Depth-First Search
def dfs(state, depth):
    if depth > L:
        return False

    if is_goal(state):
        return True

    actions = get_possible_actions(state)
    for action in actions:
        new_state = perform_move(state, action)
        if dfs(new_state, depth + 1):
            # print(new_state[0])
            # print()
            for i in range(3):
              print(new_state[i])
            print()
            return True

    return False

# Start DFS from the initial state
if dfs(initial_state, 0):
    print("Goal state reached!")
else:
    print("Goal state not reached within depth limit.")
