#!/usr/bin/env python3

import math
import sys


def max_two_digit_number(s):
	best_first = -1
	best_second = -1
	best_value = -1

	for c in s:
		d = int(c)

		if best_first != -1:
			value = best_first * 10 + d
			if value > best_value:
				best_value = value

		if d > best_first:
			best_first = d

	return best_value


if __name__ == '__main__':
	
	total_joltage = 0

	for line, bank in enumerate(sys.stdin.readlines()):
		jolts = max_two_digit_number(bank.strip())
		total_joltage += jolts
		print(f'{line=} {bank=} {jolts=} {total_joltage=}')

	print(f'{total_joltage}')
