#!/usr/bin/env python3

import sys


MAX = 99 + 1
STARTING_POINT = 50
COUNT_ON = 0

SIGN = {'L': -1, 'R': 1}


pointer = STARTING_POINT
counter = 0


for step, line in enumerate(sys.stdin.readlines()):
	number = SIGN[line[0]] * int(line[1:])
	pointer = (pointer + number) % MAX

	if pointer == COUNT_ON:
		counter += 1

	print(f'{step=} {line=} {number=} {pointer=} {counter=}')

print(f'Done. {counter=}')
