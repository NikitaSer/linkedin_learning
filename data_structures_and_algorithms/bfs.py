"""
Breadth-first search (BFS) is an algorithm for searching a tree data structure
for a node that satisfies a given property. It starts at the tree root and explores
all nodes at the present depth prior to moving on to the nodes at the next depth level.
"""
import read_maze
import helpers
from queue_ll import Queue

def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return helpers.get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = helpers.offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if helpers.is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell
    return None


if __name__ == "__main__":
    maze_file_path = "C:/Users/mykyta.serhiienko/Desktop/nik/linkedin_learning_courses/linkedin_learning/data_structures_and_algorithms/mazes/mini_maze_bfs.txt"
    challenge_maze = "C:/Users/mykyta.serhiienko/Desktop/nik/linkedin_learning_courses/linkedin_learning/data_structures_and_algorithms/mazes/challenge_maze.txt"

    # Test_1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test_2
    maze = read_maze.read_maze(maze_file_path)
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test_3
    maze = read_maze.read_maze(maze_file_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
