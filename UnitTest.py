from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ('aabaaaacaabc', 2, 8), 2: ('a', 1, -1), 3: ('ccbaa', 3, -1)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        s, k, output = self.__testCases[1]
        result = self.__obj.takeCharacters(s = s, k = k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        s, k, output = self.__testCases[2]
        result = self.__obj.takeCharacters(s = s, k = k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        s, k, output = self.__testCases[3]
        result = self.__obj.takeCharacters(s = s, k = k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()