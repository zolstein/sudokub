#!/usr/bin/env python
import itertools as it

from intbitset import intbitset

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

row_viz = [intbitset() for _ in range(9)]
col_viz = [intbitset() for _ in range(9)]
box_viz = [intbitset() for _ in range(9)]

def compute_visibility():
    for i in range(9):
        row_start = i * 9
        row_cells = range(row_start, row_start + 9)
        for cell in row_cells:
            row_viz[i].add(grid[cell])

        col_start = i
        col_cells = range(col_start, col_start + 81, 9)
        for cell in col_cells:
            col_viz[i].add(grid[cell])

        corner = i // 3 * 27 + i % 3 * 3
        box_cells_1 = range(corner, corner + 3)
        box_cells_2 = range(corner + 9, corner + 12)
        box_cells_3 = range(corner + 18, corner + 21)
        box_cells = it.chain(box_cells_1, box_cells_2, box_cells_3)
        for cell in box_cells:
            box_viz[i].add(grid[cell])

def compute_cells_seen(index):
    if grid[index]:
        return None

    row = index // 9
    col = index % 9
    box = index // 27 * 3 + index % 9 // 3

    return (row_viz[row], col_viz[col], box_viz[box])

compute_visibility()
cells_seen = [compute_cells_seen(i) for i in range(81)]
one_to_nine = intbitset(range(1, 10))

def copy(grid):
    return grid[:]

get_conflicts_calls = 0

solutions = []

def solve(grid, start=0):
    global get_conflicts_calls
    for n in range(start, 81):
        if not grid[n]:
            get_conflicts_calls += 1
            row, col, box = cells_seen[n]
            conflicts = row | col | box
            for v in one_to_nine - conflicts:
                # Try v in position n
                grid[n] = v
                row.add(v)
                col.add(v)
                box.add(v)
                # Recursive call
                solve(grid, n + 1)
                # Remove v and continue
                grid[n] = 0
                row.remove(v)
                col.remove(v)
                box.remove(v)
            return
    return solutions.append(copy(grid))

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
for s in solutions:
    print_grid(s)

print(f"get_conflicts: {get_conflicts_calls}")

