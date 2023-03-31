#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

status = int(input("Please input status code:"))

def http_error(status):
	match status:
		case 400:
			return "Bad request"
		case 404:
			return "Not found"
		case 418:
			return "I'm a teapot"
		case _:
			return "Something's wrong with the internet"

print(http_error(status))

