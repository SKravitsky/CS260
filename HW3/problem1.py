#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW3

import sys

def fib(x):
	if x < 2:
		return 1
	else:
		return fib(x-1) + fib(x-2)

def main():
	x = int(sys.argv[1])
	y = fib(x)
	print y

if __name__ == '__main__':
	main()
