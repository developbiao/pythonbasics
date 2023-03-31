#!/usr/bin/env python3
#! -*- coding:utf-8 -*-

import sys

list = [1, 2, 3, 4, 5, 6]

it = iter(list)

while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()



