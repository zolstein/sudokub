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

grid = [cell for row in grid for cell in row]
    
def is_possible(grid, index, v):
    row_start = index // 9 * 9
    row_pairs = range(row_start, row_start + 9)
    col_start = index % 9
    col_pairs = range(col_start, col_start + 81, 9)
    corner = index // 27 * 27 + (index % 9) // 3 * 3
    box_pairs_1 = range(corner, corner + 3)
    box_pairs_2 = range(corner + 9, corner + 12)
    box_pairs_3 = range(corner + 18, corner + 21)
    pairs = it.chain(row_pairs, col_pairs, box_pairs_1, box_pairs_2, box_pairs_3)
    return not any(grid[n] == v for n in pairs)

def copy(grid):
    return grid[:]

def solve(grid, start=0):
    # solutions = []
    for n in range(start, 9 * 9):
        if not grid[n]:
            for v in range(1, 10):
                if is_possible(grid, n, v):
                    grid[n] = v
                    # solutions.extend(solve(grid, n + 1))
                    if solve(grid, n + 1):
                        return grid
                    grid[n] = 0
            # return solutions
            return None
    #return [copy(grid)]
    return grid

def print_grid(grid):

    def chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    for row in chunks(grid, 9):
        print(" ".join((str(x) for x in row)))

print("before")
print_grid(grid)

solve(grid)

print("after")
print_grid(grid)
