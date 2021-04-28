###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #3
# Program: test_cube.py
###############################

import unittest
import avg


class testAvg(unittest.TestCase):


	def test_empty_list(self):
		print("\nIMPORTANT: Keep in mind that test_empty_list will cause a failure if the list is NOT empty")
		array = input("Enter a list of numbers (i.e. [1, 2, 3, 4, 5]) for empty list testing: ")
		x = 0
		array = array.replace("[", "")
		array = array.replace("]", "")
		newArray = array.split(", ")
		while x < len(newArray):
			if newArray[x] != '':
				newArray[x] = float(newArray[x])
			else:
				newArray = []
			x = x + 1
		with self.assertRaises(ZeroDivisionError): avg.getAverage(newArray)
		print("There is a Zero Division Error ... You can't get the average of nothing")


	def test_is_list(self):
		print("\nIMPORTANT: Keep in mind that test_empty_list will cause a failure if the list is NOT empty")
		array = input("Enter a some numbers as a list (i.e. [1, 2, 3, 4] or as a integer (i.e. 1) for is list testing: ")
		if array[0] == "[":
			x = 0
			array = array.replace("[", "")
			array = array.replace("]", "")
			newArray = array.split(", ")
			while x < len(newArray):
				newArray[x] = float(newArray[x])
				x = x + 1
		else:
			newArray = int(array)
		with self.assertRaises(TypeError): avg.getAverage(newArray)
		print("There is a Type Error ... You did not enter a list")

	def test_validity(self):
		array = input("\nEnter a some numbers as a list (i.e. [1, 2, 3, 4] for validity testing: ")
		expectedAnswer = input("Enter the expected average from the previous list: ")
		expectedAnswer = int(expectedAnswer)
		x = 0
		array = array.replace("[", "")
		array = array.replace("]", "")
		newArray = array.split(", ")
		while x < len(newArray):
			newArray[x] = float(newArray[x])
			x = x + 1
		programAnswer = avg.getAverage(newArray)
		self.assertTrue(expectedAnswer == programAnswer)

if __name__ == '__main__':
	unittest.main()
