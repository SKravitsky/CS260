#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW3

import timeit
from problem1 import fib
from problem2 import fib_memo

def test_problem1(n):
	return fib(n)


def test_problem2(n):
	return fib_memo(n)


if __name__ == "__main__":
	txt_file = 'mydata.txt'
	formatting = '{:<5} {:<20} {:<20} {:<20}'	

	formatting2 = '{:<5} {:<20}'	

	outfile = open(txt_file, 'w')
	
	for num_vals in range(41):
		problem1_timer = timeit.Timer('test_problem1(num_vals)', 'from __main__ import test_problem1, num_vals')
		problem1_delta = problem1_timer.timeit(1)

		problem2_timer = timeit.Timer('test_problem2(num_vals)', 'from __main__ import test_problem2, num_vals')
		problem2_delta = problem2_timer.timeit(1)
		
		num = test_problem2(num_vals)
		
		outfile.write(formatting2.format(num_vals, problem2_delta))
		outfile.write("\n")

		print formatting.format(num_vals, num, problem1_delta, problem2_delta)

	outfile.close()
