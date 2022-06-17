"""
A* is a graph traversal and path search algorithm, which is often used in many fields
of computer science due to its completeness, optimality, and optimal efficiency.
One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes
in memory.

Uses a priority queue containing f-values (distance from the current  cell to the goal) and (i, j) tuples along with
dictionaries for predecessors and g-values (distance from the current cell to the start)

g-value - best distance from start to the current cell.
h-value - heuristic distance from the current cell to the destination.
f-value - the sum of the "g" and "h", representing the probable optimal value or minimum
distance based on the heuristic used.
"""
import helpers
import read_maze
from priority_queue import PriorityQueue


def h_value(a, b):
    """Calculates the heuristic (Manhattan distance) between two pairs of grid coordinates"""
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return helpers.get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = helpers.offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if helpers.is_legal_pos(maze, neighbour) and neighbour not in g_values:
                g_value_neighbour = g_values[current_cell] + 1
                g_values[neighbour] = g_value_neighbour
                f_value_neighbour = g_value_neighbour + h_value(goal, neighbour)
                pq.put(neighbour, f_value_neighbour)
                predecessors[neighbour] = current_cell


if __name__ == "__main__":
    maze_file_path = "C:/Users/mykyta.serhiienko/Desktop/nik/linkedin_learning_courses/linkedin_learning" \
                     "/data_structures_and_algorithms/mazes/mini_maze_bfs.txt "
    challenge_maze = "C:/Users/mykyta.serhiienko/Desktop/nik/linkedin_learning_courses/linkedin_learning" \
                     "/data_structures_and_algorithms/mazes/challenge_maze.txt "

    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze.read_maze(maze_file_path)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze.read_maze(maze_file_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
