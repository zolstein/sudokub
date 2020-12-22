#!/usr/bin/python
import itertools as it

grid = [
 [0, 0, 3, 0, 0, 0, 0, 9, 0],
 [0, 0, 0, 0, 0, 9, 5, 0, 0],
 [0, 0, 0, 8, 4, 3, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 7, 0, 2],
 [0, 0, 0, 0, 0, 6, 0, 0, 0],
 [9, 0, 2, 0, 3, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 8, 0, 0, 0],
 [6, 0, 5, 0, 0, 0, 9, 0, 7],
 [1, 0, 7, 0, 0, 0, 2, 5, 0],
]

# grid = [cell for row in grid for cell in row]
    
def is_possible(grid, x, y, v):
    row_pairs = ((i, y) for i in range(9))
    col_pairs = ((x, j) for j in range(9))
    x_corner = x // 3 * 3
    y_corner = y // 3 * 3
    box_pairs = ((x_corner + i_off, y_corner + j_off) 
                 for i_off in range(3) 
                 for j_off in range(3))
    pairs = it.chain(row_pairs, col_pairs, box_pairs)
    return not any(grid[i][j] == v for (i, j) in pairs)

def copy(grid):
    return [row[:] for row in grid]

def get(grid, x, y):
    return grid[x][y]
    # return grid[x * 9 + y]

def solve(grid, start=0):
    # solutions = []
    for n in range(start, 9 * 9):
        x = n // 9
        y = n % 9
        if not grid[x][y]:
            for v in range(1, 10):
                if is_possible(grid, x, y, v):
                    grid[x][y] = v
                    # solutions.extend(solve(grid, n + 1))
                    if solve(grid, n + 1):
                        return grid
                    grid[x][y] = 0
            # return solutions
            return None
    #return [copy(grid)]
    return grid

def print_grid(grid):

    # def chunks(l, n):
        # for i in range(0, len(l), n):
            # yield l[i:i + n]

    # for row in chunks(grid, 9):
    for row in grid:
        print(" ".join((str(x) for x in row)))

print("before")
print_grid(grid)

solve(grid)

print("after")
print_grid(grid)
