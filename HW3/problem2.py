#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW3

import sys

memo = {0:1, 1:1}
def fib_memo(x):	
	if x not in memo:
		memo[x] = fib_memo(x-1) + fib_memo(x-2)
		return memo[x]
	return memo[x]

def main():
	x = int(sys.argv[1])
	y = fib_memo(x)
	print y
	memo = {0:1, 1:1}



if __name__ == '__main__':
	main()
