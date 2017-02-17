from hell_triangle import HellTriangle
from unittest import TestCase


class TestHellTriangle(TestCase):
    def test_simple_triangle(self):
        """Maximum sum should be equals to 26."""
        tree = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
        max_sum = HellTriangle(tree).get_max_sum()
        self.assertEqual(max_sum, 26)

    def test_tree_not_triangle(self):
        """Invalid triangle should raise TypeError."""
        tree = [[6], [3, 5], [9, 7, 1], [4, 6, 8]]
        with self.assertRaises(TypeError):
            HellTriangle(tree).get_max_sum()

    def test_balanced_tree(self):
        """Maximum sum should be equals to 5."""
        tree = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
        max_sum = HellTriangle(tree).get_max_sum()
        self.assertEqual(max_sum, 5)

    def test_tree_height_one(self):
        """Maximum sum should be equals to 1."""
        tree = [[1]]
        max_sum = HellTriangle(tree).get_max_sum()
        self.assertEqual(max_sum, 1)

    def test_empty_array(self):
        """Empty array should raise TypeError."""
        tree = []
        with self.assertRaises(TypeError):
            HellTriangle(tree).get_max_sum()

    def test_tree_empty_nodes(self):
        """Nodes with empty values should raise TypeError."""
        tree = [[], []]
        with self.assertRaises(TypeError):
            HellTriangle(tree).get_max_sum()

    def test_large_triangle(self):
        """Maximum sum should be equals to 10044."""
        tree = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4], [7, 5, 9, 1, 6],
                [9, 9, 9, 9, 900, 8], [8, 7, 87, 10000, 999, 666, 0]]
        max_sum = HellTriangle(tree).get_max_sum()
        self.assertEqual(max_sum, 10044)

    def test_negative_values(self):
        """Maximum sum should be equals to -4."""
        tree = [[-1], [-1, -1], [-1, -1, -1], [-1, -1, -1, -1]]
        max_sum = HellTriangle(tree).get_max_sum()
        self.assertEqual(max_sum, -4)

    def test_zeroed_tree(self):
        """Maximum sum should be equals to 0."""
        tree = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
        max_sum = HellTriangle(tree).get_max_sum()
        self.assertEqual(max_sum, 0)