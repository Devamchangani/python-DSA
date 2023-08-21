from collections import deque
import numpy as np

# Function to check if the given state is the goal state
def is_goal_state(state, goal_state):
    return state == goal_state

# Function to get all possible states by swapping the blank tile with its neighbors
def get_possible_states(state):
    possible_states = []
    blank_index = state.index(0)

    # Possible moves: left, right, up, down
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        new_x, new_y = blank_index // 3 + dx, blank_index % 3 + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = state[:]
            new_blank_index = new_x * 3 + new_y
            new_state[blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[blank_index]
            possible_states.append(new_state)

    return possible_states

# Function to perform BFS search on the 8-puzzle problem
def bfs_search(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if is_goal_state(state, goal_state):
            return path

        visited.add(tuple(state))

        for next_state in get_possible_states(state):
            if tuple(next_state) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Example usage:
if __name__ == "__main__":
    initial_state = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    result_path = bfs_search(initial_state, goal_state)

    if result_path:
        print("Path to goal state:")
        for state in result_path:
           a = np.array(state)
           print(a.reshape((3,3)))
           print("")
    else:
        print("Goal state not reachable.")