###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #3
# Program: test_cube.py
###############################

import unittest
import fullname


class testName(unittest.TestCase):


	def test_is_empty(self):
		print("\nfor test_is_empty")
		first = input("Enter the first name: ")
		last = input(" Enter the last name: ")
		name = fullname.combineName(first, last)
		name = name.replace(" ", "")
		self.assertIsNot(name, "")

	def test_allowed_characters(self):
		print("\nFor test_allowed_characters (not allowed characters: ! @ # $ % ^ &")
		first = input("Enter the first name: ")
		last = input(" Enter the last name: ")
		name = fullname.combineName(first, last)
		desiredName = len(name)
		name = name.replace("!", "")
		name = name.replace("@", "")
		name = name.replace("#", "")
		name = name.replace("$", "")
		name = name.replace("%", "")
		name = name.replace("^", "")
		name = name.replace("&", "")
		legalName = len(name)
		self.assertEqual(desiredName, legalName)

	def test_character_limit(self):
		print("\nfor test_character_limit")
		first = input("Enter the first name: ")
		last = input(" Enter the last name: ")
		name = fullname.combineName(first, last)
		nameLength = len(name)
		self.assertLess(nameLength, 16)

	


if __name__ == '__main__':
	unittest.main()
