#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW2

from cell import Cell


def list_concat_copy(a,b):
	final_list = Cell(a.data)
	new_list = final_list

	while a.next != None:
		new_list.next = Cell(a.next.data)
		new_list = new_list.next
		a = a.next

	new_list.next = Cell(b.data)
	new_list = new_list.next

	while b.next != None:
		new_list.next = Cell(b.next.data)
		new_list = new_list.next
		b = b.next

	return final_list

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

	c = list_concat_copy(a, b) 

	print 'The new list contains the following values:'
	print_list(c)
	print

	print 'List "A" still contains the following values:'
	print_list(a)
	
	print 'List "B" still contains the following values:'
	print_list(b)
