#!/usr/bin/env python3

import copy
import sys


def build_grid(lines):
	chars = {'@': 1, '.': 0}

	y = len(lines)
	x = len(lines[0])
	empty_row = [0] * (x + 1)  # Stripped \n

	grid = []
	grid.append(empty_row)
	for l in lines:
		row = [0] + [chars[c] for c in l.strip()] + [0]
		grid.append(row)
	grid.append(empty_row)

	return grid


def count_available_rolls(grid, max_neighbours=3):
	marked_grid = copy.deepcopy(grid)

	y = len(grid) - 2
	x = len(grid) - 2

	available_rolls = 0
	for i in range(1, y + 1):
		for j in range(1, x + 1):
			if grid[i][j] == 0:
				continue

			neighbours_count = \
				grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + \
				grid[i][j-1] + 0 + grid[i][j+1] + \
				grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]

			if neighbours_count <= max_neighbours:
				marked_grid[i][j] = 'x'
				available_rolls += 1

	return marked_grid, available_rolls


def print_grid(grid):
	print('\n'.join(''.join(str(c) for c in l[1:len(l) - 1]) 
		  for l in grid[1:len(grid) - 1]))
	print()


if __name__ == '__main__':
	lines = sys.stdin.readlines()
	grid = build_grid(lines)

	print_grid(grid)

	marked_grid, available_rolls = count_available_rolls(grid)

	print_grid(marked_grid)

	print(f'{available_rolls=}')
