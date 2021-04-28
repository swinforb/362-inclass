###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #3
# Program: test_cube.py
###############################

import unittest
import cube


class TestCube(unittest.TestCase):


	def test_type(self):
		print("IMPORTANT: Keep in mind that test_type will cause a failure if the types are correct (int)")
		val = input("Enter a number for type testing (if you want an int enter n before the number like n5 for 5: ")
		if val[0] == "n":
			val = val.replace('n', '')
			val = float(val)
			val = round(val)
		with self.assertRaises(TypeError): cube.VolumeOfCube(val)
		print("There is a Type Error ... You chose to enter a string")


	def test_negative(self):
		val = input("Enter a number for negative testing: ")
		val = float(val)
		result = cube.VolumeOfCube(val)
		message = "A cube may not have negative dimensions"
		self.assertLess(0, result, message)

	def test_whole_number(self):
		val = input("Enter a number for whole number testing: ")
		valInt = float(val)
		valInt = round(valInt)
		valFlt = float(val)
		message = "A floating point number was entered, not a whole number"
		self.assertEqual(valInt, valFlt, message)


if __name__ == '__main__':
	unittest.main()
