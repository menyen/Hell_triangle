Language:
    - Python. The choice was made because the language already comes with a test framework built-in, easy array manipulation and it is easier to run, test and import helpful modules. As a friend of mine once said, the language already comes with batteries and it is ready to use, meaning that I don't need to struggle in setting up my dev environment, I just need to worry about the code.

Run:
    - If you just want to run the code and see it solve the example shown in the problem description, just go inside hell_triangle folder through a terminal and run: python hell_triangle.py
    - It will display the result in the command line

Tests:
    - unittest framework from Python was used to implement the tests
    - Go to hell_triangle folder through a terminal
    - Run: python -m unittest tests.test_hell_triangle.TestHellTriangle

Algorithm:
    - Depth-first search with recursion. The Hell Triangle problem is similar to the DFS problem in the aspect that the search should start at the root and it should explore as far as possible along each branch before backtracking. One of the main differences is that Hell Triangle doesn't need to be concerned if a node was already visited. Neighbors of the current node gets visited indifferently, even if it was already visited.
    - This algorithm has its limitation, as it was made with recursion, it consumes a bit more memory than its iterative version.
