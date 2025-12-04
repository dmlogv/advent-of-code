#!/usr/bin/env python3

import copy
import sys


MAX_GENS = 10_000


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


def eject_available_rolls(grid, max_neighbours=3):
	y = len(grid) - 2
	x = len(grid) - 2

	ejected_rolls = 0
	for i in range(1, y + 1):
		for j in range(1, x + 1):
			if grid[i][j] == 0:
				continue

			neighbours_count = \
				grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + \
				grid[i][j-1] + 0 + grid[i][j+1] + \
				grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]

			if neighbours_count <= max_neighbours:
				grid[i][j] = 0
				ejected_rolls += 1

	return ejected_rolls


def print_grid(grid):
	print('\n'.join(''.join(str(c) for c in l[1:len(l) - 1]) 
		  for l in grid[1:len(grid) - 1]))
	print()


if __name__ == '__main__':
	lines = sys.stdin.readlines()
	grid = build_grid(lines)

	print_grid(grid)

	total_rolls = 0
	for i in range(MAX_GENS):
		ejected_rolls = eject_available_rolls(grid)
		total_rolls += ejected_rolls

		if ejected_rolls == 0:
			break

		print_grid(grid)
		print(f'{ejected_rolls=}')
	else:
		raise RuntimeError(f'{MAX_GENS=} exceeded')

	print(f'{total_rolls=}')
