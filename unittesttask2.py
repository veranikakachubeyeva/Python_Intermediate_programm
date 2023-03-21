import unittest
from task2counteroccuriencies import count_occuriencies


class TestCounterOfOccuriencies(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_occuriencies(b"abad "), {('d', 1), ('b', 1), ('a', 1)})
    
    def test_occuriencies_simple(self):
        self.assertEqual(count_occuriencies(b"abaaaaaaad "), {('a', 7)})

    def test_occuriencies(self):
        self.assertEqual(count_occuriencies(b"abbbbbbbaaaaaaad "), {('a', 7), ('b', 7)})
        
    def test_occuriencies_with_duplicates(self):
            self.assertEqual(count_occuriencies(b"abbbbbbbcbbbbbbbd "), {('b', 7)})

if __name__ == '__main__':
    unittest.main()    