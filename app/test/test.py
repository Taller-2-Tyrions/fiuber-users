import unittest

# TESTS
class UsersTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(1,1)

	def test2(self):
		self.assertEqual(1,2)

if __name__ == '__main__':
	try:
		unittest.main()
	except Exception as err:
		print(str(err))
	exit = input("Exit")