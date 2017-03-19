#!/usr/bin/python
# example.py - an example of "including" (importing) a user-defined type,
#		and of using the timeit function
#
# 1/07
#
import random
import timeit

import cell

f = cell.Cell(6)
g = cell.Cell(7,f)
h = cell.Cell(8,g)

i = cell.Cell(9)
j = cell.Cell(10,i)
k = cell.Cell(11,j)

z = cell.list_concat_copy(h,k)
print_list(z)
print '-----------------'
#print_list(c)


#print_list(c)
#g = cell.Cell(11,f)
#print_list(c



A = cell.Cell(12, cell.Cell(13))
B = cell.Cell(14, cell.Cell(15, cell.Cell(16)))
print 'Before concatenation, A is: {} and B is {}'.format(
	A.__str__(), B.__str__())
print 'After concatenation, the new list is: {}'.format(
	cell.list_concat_copy(A, B).__str__())
