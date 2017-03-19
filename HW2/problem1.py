#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW2

from cell import Cell


def list_concat(a,b):
	value = a

	while value.next != None:
		value = value.next

	value.next = b
	return a

def print_list(self):
	node = self
	while node != None:
		print node.data
		node = node.next

if __name__ == "__main__":
	b = Cell(5, Cell(6))
	a = Cell(3, Cell(4))

	print 'List "A" contains the following values:'
	print_list(a)
	
	print 'List "B" contains the following values:'
	print_list(b)

	c = list_concat(a, b) 

	print 'The new list contains the following values:'
	print_list(c)
