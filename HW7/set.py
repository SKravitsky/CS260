#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW6

import sys

class Node:
	def __init__(self, parent, depth):
		self.parent = parent
		self.depth = depth

def Initialize(value):
	the_set = {}
	parent = None
	depth = 0

	for item in value:
		the_set[item] = Node(parent, depth)
	return the_set

def Find(the_set, value):
	if the_set[value].parent is None:
		return value
	else:
		the_set[value].parent = Find(the_set, the_set[value].parent)
		return the_set[value].parent

def Merge(the_set, value1, value2):
	set_1 = Find(the_set, value1)
	set_2 = Find(the_set, value2)

	if the_set[set_1].depth <= the_set[set_2].depth:
		the_set[set_1].parent = set_2
		the_set[set_2].parent = None
		the_set[set_2].depth = the_set[set_2].depth + the_set[set_1].depth + 1
	else:
		the_set[set_2].parent = set_1
		the_set[set_1].parent = None
		the_set[set_1].depth = the_set[set_1].depth + the_set[set_2].depth + 1

