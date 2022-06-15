"""
Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts
at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as
possible along each branch before backtracking. So the basic idea is to start from the root or any arbitrary node and
mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node.
Then backtrack and check for other unmarked nodes and traverse them. Finally, print the nodes in the path.
"""

import helpers
import read_maze
from stack import Stack


def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return helpers.get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = helpers.offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if helpers.is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                stack.push(neighbour)
                predecessors[neighbour] = current_cell
    return None


if __name__ == "__main__":
    maze_file_path = "C:/Users/mykyta.serhiienko/Desktop/nik/linkedin_learning_courses/linkedin_learning/data_structures_and_algorithms/mazes/mini_maze_dfs.txt"
    challenge_maze = "C:/Users/mykyta.serhiienko/Desktop/nik/linkedin_learning_courses/linkedin_learning/data_structures_and_algorithms/mazes/challenge_maze.txt"

    # Test_1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test_2
    maze = read_maze.read_maze(maze_file_path)
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test_3
    maze = read_maze.read_maze(maze_file_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
