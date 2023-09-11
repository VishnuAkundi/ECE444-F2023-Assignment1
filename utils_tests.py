from utils import *
import unittest

class tests(unittest.TestCase):
	def test_reversed(self):
		u = utils()
		self.assertFalse(u.reversed("2023"))
		self.assertFalse(u.reversed(2023.0))
		self.assertEqual(u.reversed(2023),3202)
		self.assertEqual(u.reversed(-2023), -3202)
	def test_formatter(self):
		u = utils()
		self.assertFalse(u.formatter(2.0))
		self.assertFalse(u.formatter("2"))
		self.assertEqual(u.formatter(2),('0b10','02'))
        	self.assertEqual(u.formatter(-2),('-0b10','-02'))
		self.assertEqual(u.formatter(39), ('0b100111', '047'))
if __name__ == "__main__":
    unittest.main()
