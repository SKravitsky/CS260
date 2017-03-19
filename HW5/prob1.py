#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW5

import math
import random
import timeit

def swap(h, x, y):
	temp = h[x]
	h[x] = h[y]
	h[y] = temp

def downheap(h, l, i):
	leftIndex = i * 2 + 1
	if (leftIndex >= l):
		return

	x = leftIndex
	rightIndex = i * 2 + 2

	if (rightIndex < l and h[leftIndex] < h[rightIndex]):
		x = rightIndex
	if h[i] < h[x]:
		swap(h, i, x)
		downheap(h, l, x)

def heaping(h, l):
	count = int((l - 1) - 1) / int(2)
	while (count >= 0):
		downheap(h, l, count)
		count = count - 1

def make_heap(Nodes):
	heap = []
	
	for x in range(0, Nodes):
		rand = random.randint(1, 500)
		heap.append(rand)
	
	heaping(heap, len(heap))
	return heap

if __name__ == '__main__':
	for n in range(1, 11):
		n = n * 10000
		time = timeit.Timer('make_heap(n)', 'from __main__ import make_heap, n')	
		delta = time.timeit(1)
		print n, delta



