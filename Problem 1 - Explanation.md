# Square Root of an Integer

## Time Complexity
The provided solution is of time complexity ***O(log2(n))*** in the worst case scenario, where *n* is the total number of possible square roots ranging from 1 until X (the value whose square root we are computing). This was achieved by implementing the solution as a recursive binary search. At each step, the possible space of square roots is halved until the (closest) solution is found. Worst case scenario is has to recurse to the lowest possible level.

## Space Complexity
This particular implementation stores little in memory. The recursion does add to the function stack but it does so independently of *n*. Hence, the space complexity is ***O(1)***.