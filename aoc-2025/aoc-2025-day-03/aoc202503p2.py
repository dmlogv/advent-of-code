#!/usr/bin/env python3

import math
import sys


def max_k_digit_number(s, k=12):
	stack = []
	to_remove = len(s) - k

	for c in s:
		d = int(c)
		while stack and stack[-1] < d and to_remove > 0:
			stack.pop()
			to_remove -= 1
		stack.append(d)

	return sum(d * 10**i for i, d in enumerate(stack[:k][::-1]))


if __name__ == '__main__':
	
	total_joltage = 0

	for line, bank in enumerate(sys.stdin.readlines()):
		jolts = max_k_digit_number(bank.strip())
		total_joltage += jolts
		print(f'{line=} {bank=} {jolts=} {total_joltage=}')

	print(f'{total_joltage}')
