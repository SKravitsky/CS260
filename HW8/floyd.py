#!/usr/bin/python
#Steven Kravitsky
#CS260
#HW8

import fileinput

numberOfLines = sum(1 for line in fileinput.input())


parent = {}
distance = {}
for x in xrange(numberOfLines):
	parent[x] = dict.fromkeys(xrange(numberOfLines), None )

for x in xrange(numberOfLines):
	distance[x] = dict.fromkeys(xrange(numberOfLines), float("inf"))

for i in xrange(numberOfLines):
	for j in xrange(numberOfLines):
		if i is j:
			distance[i][j] = 0

for line in fileinput.input():
	data = line.split()

	for x in xrange(1,len(data)):
		point = data[x].split(",")
		u = int(data[0])
		v = int(point[0])
		weight = int(point[1])

		distance[u][v] = weight
		distance[v][u] = weight

		parent[u][v] = u
		parent[v][u] = v

for k in xrange(numberOfLines):
	for i in xrange(numberOfLines):
		for j in xrange(numberOfLines):
			if distance[i][j] > distance[i][k] + distance[k][j]:
				distance[i][j] = distance[i][k] + distance[k][j]
				parent[i][j] = k

print "Distance:"
print " ",
for x in xrange(numberOfLines):
	print repr(x).rjust(4),
print "\n"

for i in xrange(numberOfLines):
	print i,
	for j in xrange(numberOfLines):
		print repr(distance[i][j]).rjust(4),
	print
print

print "Predecessor:"
print " ",
for x in xrange(numberOfLines):
	print repr(x).rjust(4),
print "\n"

for i in xrange(numberOfLines):
	print i,
	for j in xrange(numberOfLines):
		print repr(parent[i][j]).rjust(4),
	print













