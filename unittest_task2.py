import unittest
from task2_counter_occuriencies import count_occuriencies


class TestCounterOfOccuriencies(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_occuriencies(b"abad"), {('d', 1), ('b', 1), ('a', 1)})
    
    def test_occuriencies_simple(self):
        self.assertEqual(count_occuriencies(b"abaaaaaaad"), {('a', 7)})

    def test_occuriencies(self):
        self.assertEqual(count_occuriencies(b"abbbbbbbaaaaaaad"), {('a', 7), ('b', 7)})
        
    def test_occuriencies_with_duplicates(self):
            self.assertEqual(count_occuriencies(b"abbbbbbbcbbbbbbbd"), {('b', 7)})
    
    def test_occuriencies_empty_file(self):
            self.assertEqual(count_occuriencies(b""), "File is empty")

    def test_occuriencies_one_symbol(self):
            self.assertEqual(count_occuriencies(b"a"), {('a', 1)})
            
    def test_occuriencies_two_symbols(self):
            self.assertEqual(count_occuriencies(b"a "), {(" ", 1), ('a', 1)})
            
    def test_occuriencies_several_symbols(self):
            self.assertEqual(count_occuriencies(b"acd"), {('c', 1), ('a', 1), ('d', 1)})   
    
    def test_occuriencies_several_same_symbols(self):
            self.assertEqual(count_occuriencies(b"aaa"), {('a', 3)})
    
    {('q', 3)}     

if __name__ == '__main__':
    unittest.main()    