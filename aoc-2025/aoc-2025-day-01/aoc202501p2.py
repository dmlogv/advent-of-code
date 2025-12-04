#!/usr/bin/env python3

import itertools
import sys


STARTING_POINT = 50
COUNT_ON = 0

SIGN = {'L': 'left', 'R': 'right'}


class Digit:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f'<{self.__class__.__name__} {self.value=}>'


class Dial:
	def __init__(self, min, max):
		self.max = max
		self.start = None
		self.pointer = None
		d = None

		for i, v in enumerate(range(min, self.max + 1)):
			d = Digit(v, self.pointer, None)
			if i == 0:
				self.start = d
			if self.pointer:
				self.pointer.right = d
			self.pointer = d
		self.pointer.right = self.start
		self.start.left = self.pointer

	def __repr__(self):
		return  f'<{self.__class__.__name__} {self.start=} {self.pointer=}>'

	def left(self):
		self.pointer = self.pointer.left

	def right(self):
		self.pointer = self.pointer.right

	def set(self, v):
		for _ in range(self.max + 1):
			if self.pointer.value == v:
				return
			self.left()
		else:
			raise ValueError(f'{v=} not found')


if __name__ == '__main__':
	dial = Dial(0, 99)
	dial.set(STARTING_POINT)


	counter = 0
	for step, line in enumerate(sys.stdin.readlines()):
		direction = SIGN[line[0]]
		steps = int(line[1:])

		while steps:
			getattr(dial, direction)()
			if dial.pointer.value == COUNT_ON:
				counter += 1
			steps -= 1
			
		print(f'{step=} {line=} {direction=} {steps=} {dial=} {counter=}')

	print(f'Done. {counter=}')
