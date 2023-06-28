""" When testing a function that is supposed to return the sorted version of a list of integers, it is important to consider various scenarios to ensure the function behaves correctly. Here are some test cases to consider:"""

import unittest

def sort_list(nums):
    # Your implementation of the sorting function goes here
    return sorted(nums)

class SortListTestCase(unittest.TestCase):
    def test_sort_list(self):
        test_cases = [
            ([4, 2, 1, 3], [1, 2, 3, 4]),
            ([], []),
            ([5], [5]),
            ([10, -5, 8, -2, 0], [-5, -2, 0, 8, 10]),
            ([3, 2, 5, 2, 1, 5], [1, 2, 2, 3, 5, 5]),
            ([1000, 100, 10, 1], [1, 10, 100, 1000]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
        ]

        for nums, expected_output in test_cases:
            print(f"Input: {nums}")
            print(f"Expected Output: {expected_output}")
            self.assertEqual(sort_list(nums), expected_output)
            print()

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
