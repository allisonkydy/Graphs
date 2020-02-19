'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
'''

from util import Stack

def get_neighbors(vertex, graph_matrix):
    col = vertex[0]
    row = vertex[1]
    neighbors = []
    # check north
    if row > 0 and graph_matrix[row - 1][col] == 1:
        neighbors.append((col, row - 1))
    # check south
    if row < len(graph_matrix) - 1 and graph_matrix[row + 1][col] == 1:
        neighbors.append((col, row + 1))
    # check east
    if col < len(graph_matrix[0]) - 1 and graph_matrix[row][col + 1] == 1:
        neighbors.append((col + 1, row))
    # check west
    if col > 0 and graph_matrix[row][col - 1] == 1:
        neighbors.append((col - 1, row))
    # return all directions that contain a 1
    return neighbors


def dft(col, row, matrix, visited):
    # create empty stack
    s = Stack()
    # push starting node onto stack
    s.push((col, row))
    # while stack is not empty
    while s.size() > 0:
        # pop vertex from top of stack
        v = s.pop()
        col = v[0]
        row = v[1]
        # check if vertex is visited, if not...
        if not visited[row][col]:
            # mark as visited
            visited[row][col] = True
            # push each neighbor onto the top of the stack
            for neighbor in get_neighbors((col, row), matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    # create a visited matrix of the same dimensions as the given matrix
    visited = []
    island_count = 0
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # walk through each cell of the matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # count up the connected components
            # if it has not been visited
            if not visited[row][col]:
                # when reach a 1...
                if matrix[row][col] == 1:
                    # do a DFT and mark each 1 as visited
                    visited = dft(col, row, matrix, visited)
                    # increment the counter by 1
                    island_count += 1
    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))
