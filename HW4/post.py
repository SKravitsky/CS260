#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW3

from lexer import *

def pre(tree):
	#Setting up variables for self, left, and right respectively
	t0 = tree[0]
	t1 = tree[1]
	t2 = tree[2]
	
	#Printing self
	print t0,

	#If the node is a leaf return nothing
	if t1 is None and t2 is None: 
		return
	
	#Find the prefix notation of the left and right trees
	pre(t1)
	pre(t2)
	
def inOrd(tree):
	#Setting up variables for self, left, and right respectively
	t0 = tree[0]
	t1 = tree[1]
	t2 = tree[2]	

	#If the node is a leaf, print itself then return
	if t1 is None and t2 is None: 
		print t0,
		return
	
	#Print the paranthesis for the formatting
	print "(", 
	#Traverse the left subtree
	inOrd(t1)
	#Print self
	print t0,
	#Traverse the right subtree
	inOrd(t2)
	#Print the paranthesis for the formatting
	print ")",

def post(tree):
	#Setting up variables for self, left, and right respectively
	t0 = tree[0]
	t1 = tree[1]
	t2 = tree[2]	
	
	#If the node is a leaf, print itself then return
	if t1 is None and t2 is None:
		print t0,
		return
	
	#Find the postfix notation of the left, right trees then print self
	post(t1)
	post(t2)
	print t0,

def evalTree(tree):
	#Setting up variables for self, left, and right respectively
	t0 = tree[0]
	t1 = tree[1]
	t2 = tree[2]	

	#If the node is a leaf then return its value
	if t1 is None and t2 is None: 
		return t0

	#If the node is a operator then do the operation on its left and right
	if t0 is '+':
		return int(evalTree(t1)) + int(evalTree(t2))
	elif t0 is '-':
		return int(evalTree(t1)) - int(evalTree(t2))
	elif t0 is '*':
		return int(evalTree(t1)) * int(evalTree(t2))
	elif t0 is '/':
		return int(evalTree(t1)) / int(evalTree(t2))
	elif t0 is '%':
		return int(evalTree(t1)) % int(evalTree(t2))


def main():
	while get_expression():
		
		stack = []
		tok = get_next_token()
		
		while tok:
			#If the node is a digit then append it to the stack
			if str.isdigit(tok[0]):
				node = [tok, None, None]
				stack.append(node)
			#If the node is an operator then combine it with its left and right
			#node
			else:
				rightNode = stack.pop()
				leftNode = stack.pop()
				node = [tok, leftNode, rightNode]
				stack.append(node)
			tok = get_next_token()

		tree = stack.pop()	
		print "pre: ",
		pre(tree)
		print "\nin: ",
		inOrd(tree)
		print "\npost: ",
		post(tree)
		print "\neval: ",
		print evalTree(tree), "\n"

if __name__ == '__main__':
	main()




