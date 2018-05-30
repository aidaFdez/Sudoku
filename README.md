# Sudoku
Making a sudoku generator and solver for practise.

The Python file only generates a random sudoku, printing all of it.
The Java file solves a given sudoku and can generate a sudoku if the given one is empty.

For the Java file, the input should be an array of integers going through each row, suing 0 for an empty space. For example, the following:
java sudoSolver 0 9 2 0 0 4 7 0 0 1 5 0 0 6 0 2 0 8 0 0 0 0 1 2 0 4 9 0 0 0 0 5 8 6 0 0 8 4 0 0 3 0 0 5 2 0 0 3 2 9 0 0 0 0 6 1 0 8 4 0 0 0 0 2 0 5 0 7 0 0 6 1 0 0 7 6 0 0 8 9 0

The array corresponds to the sudoku:

   -----------------------
  |   9 2 |     4 | 7     |
  | 1 5   |   6   | 2   8 |
  |       |   1 2 |   4 9 |
   -----------------------
  |       |   5 8 | 6     |
  | 8 4   |   3   |   5 2 |
  |     3 | 2 9   |       |
   -----------------------
  | 6 1   | 8 4   |       |
  | 2   5 |   7   |   6 1 |
  |     7 | 6     | 8 9   |
   -----------------------


I used an array for the sudoku, but I think an implementation with a matrix could have been easier.
I am also sure that there might be a better way to search for solutions, but a DFS was the first thing 
that came to my mind and I wanted to try some of the algorithms learnt at class. It also works pretty fast.
