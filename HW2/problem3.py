#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW2

import timeit
from cell import Cell
from problem1 import list_concat, print_list
from problem2 import list_concat_copy

def test_problem1(n):
	a = create_list(n)
	b = create_list(n)
	list_concat(a,b)


def test_problem2(n):
	a = create_list(n)
	b = create_list(n)
	list_concat_copy(a,b)


def create_list(n):
	final_list = Cell(0)
	new_list = final_list
	
	for i in range(1, n):
		new_list.next = Cell(i)
		new_list = new_list.next

	return final_list


if __name__ == "__main__":
	
	formatting = '{:<5} {:<20} {:<20}'	

	for num_vals in range(1000,16000,1000):
		problem1_timer = timeit.Timer('test_problem1(num_vals)', 'from __main__ import test_problem1, num_vals')
		problem1_delta = problem1_timer.timeit(1)

		problem2_timer = timeit.Timer('test_problem2(num_vals)', 'from __main__ import test_problem2, num_vals')
		problem2_delta = problem2_timer.timeit(1)
		
		print formatting.format(num_vals, problem1_delta, problem2_delta)

