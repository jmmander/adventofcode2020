import numpy

f = open('day3input.txt', 'r')
grid = []
for line in f:
    grid.append(line.strip('\n'))

path_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
start = (0,0)
row_len = len(grid[0])
no_rows = len(grid)


def countTrees(path):
    position = start
    total = 0
    while position[1] < no_rows:
        next_position = tuple(map(lambda i, j: i + j, path, position))
        right = next_position[0]
        down = next_position[1]
        if down < no_rows:
            if right < row_len:
                grid_val = grid[next_position[1]][next_position[0]]
            else:
                posi = right%row_len
                grid_val = grid[next_position[1]][posi]
            if grid_val == "#":
                total += 1
            position = next_position
        else:
            return total
    return total


product_list = []
for path in path_list:
    trees = countTrees(path)
    product_list.append(trees)
print(numpy.prod(product_list))