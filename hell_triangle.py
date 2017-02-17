class HellTriangle:
    def __init__(self, tree):
        """ Initializes attribute tree."""
        # max_sum is initialized as None in case the tree has negative values
        self._max_sum = None
        self._tree = tree

    def _dfs(self, i=0, j=0, partial_sum=0):
        """Function to search tree with Depth-first search algorithm.
        Once a leaf is reached, the sum of all vertices from a branch
        are compared to max_sum, which is the variable that stores the
        maximum sum found so far.
        """
        if not self._check_if_triangle():
            raise TypeError("Input is not a triangle")
        if len(self._tree) == i + 1:
            # This condition happens when a leaf is reached,
            # max_sum is then updated if it is not the current max value
            if self._max_sum is None or self._max_sum < partial_sum + self._tree[i][j]:
                self._max_sum = partial_sum + self._tree[i][j]
        else:
            # In case the "if" above is not met, dfs is applied to neighbors of node
            self._dfs(i + 1, j, self._tree[i][j] + partial_sum)
            self._dfs(i + 1, j + 1, self._tree[i][j] + partial_sum)

    def get_max_sum(self):
        """Executes dfs() with initial node in tree[0][0] and sum = 0.

        :return: maximum sum from the triangle
        """
        self._dfs()
        return self._max_sum

    def _check_if_triangle(self):
        """Checks whether the tree used as input in the class is a triangle.

        :return: True if attribute tree is a triangle and False otherwise
        """
        if not self._tree:
            return False
        if any([len(e) != i + 1 for i, e in enumerate(self._tree)]):
            return False
        return True


def main():
    tree = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
    max_sum = HellTriangle(tree).get_max_sum()
    print(max_sum)


if __name__ == "__main__":
    main()
