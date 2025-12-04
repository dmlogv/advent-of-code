#!/usr/bin/env python3

import itertools
import math
import sys


def parse_line(line):
	return line.split(',')


def parse_range(range):
	return tuple(int(v) for v in range.split('-'))


def invalid(product_id):
	s = str(product_id)
	return (s + s).index(s, 1) < len(s)


if __name__ == '__main__':
	line = sys.stdin.readline()
	ranges = parse_line(line)
	pairs = [parse_range(r) for r in ranges]

	invalid_ids = []

	for pair in pairs:
		print(pair)
		for product_id in range(pair[0], pair[1] + 1):
			print(f'{product_id}= {invalid(product_id)}')

			if invalid(product_id):
				invalid_ids.append(product_id)

	print(f'{invalid_ids=}')
	print(f'Sum is {sum(invalid_ids)}')
