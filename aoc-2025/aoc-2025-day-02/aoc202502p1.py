#!/usr/bin/env python3

import itertools
import math
import sys


def parse_line(line):
	return line.split(',')


def parse_range(range):
	return tuple(int(v) for v in range.split('-'))


def invalid(product_id):
	number_len = math.floor(math.log10(product_id)) + 1

	if number_len % 2 == 1:
		return False

	half_places = 10**(number_len / 2)

	high_digits = product_id // half_places
	low_digits = product_id % half_places

	if high_digits == low_digits:
		return True

	return False


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
