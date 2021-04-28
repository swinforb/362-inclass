###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #3
# Program: avg.py
###############################


def getAverage(a):
	x = 0
	total = 0
	divide_by = len(a)
	while x < len(a):
		total = total + a[x]
		x = x + 1
	average = total / divide_by
	print(average)
	return average

#getAverage([])
