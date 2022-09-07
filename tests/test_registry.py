import unittest


class RegistryTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, 1)

    def test2(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
