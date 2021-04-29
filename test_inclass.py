import unittest
import inclass


class testAvg(unittest.TestCase):


	def test_add_correct(self):
		num1 = input("\nEnter a number for correctness testing: ")
		num1 = float(num1)
		num2 = input("Enter another number: ")
		num2 = float(num2)
		expectedAnswer = input("Enter the expected average from the previous list: ")
		expectedAnswer = float(expectedAnswer)
		programAnswer = inclass.add(num1, num2)
		self.assertTrue(expectedAnswer == programAnswer)

	def test_subtract_validity(self):
		print("Testing 6 - 2 = 4")
		num1 = 6
		num2 = 2
		answer = inclass.subtract(num1, num2)
		self.assertEqual(4, answer)

	def test_multiply_pos_and_neg(self):
		num1 = input("\nEnter a positive number for pos*neg testing: ")
		num1 = float(num1)
		num2 = input("Enter a negative number for pos*neg testing: ")
		num2 = float(num2)
		answer = inclass.multiply(num1, num2)
		self.assertLess(answer, num1)

	def test_divide_zero(self):
		num1 = 3
		num2 = 0
		print("IF THE TEST_DIVIDE_ZERO FAILURE OCCURS, THEN IT'S ALRIGHT, WORRY IF THERE IS NOT ONE")
		with self.assertRaises(ZeroDivisionError): inclass.divide(num1, num2)
		print("THERE WAS A ZERO DIVISION ERROR")


