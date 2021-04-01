# Rotated Array Search

## Time Complexity
Similar to task #1, the time complexity of this implementation is ***O(log2(n))*** in the worst case scenario, where *n* is the length of the input list. This was achieved by (again) using recursive binary search, which splits the search space in half with every iteration. Of course there are some additional constant computational steps at each iteration (to determine the new start, mid, and end points), but as these are constant, they are ignored in out big O calculation.

## Space Complexity
Python (by default) does not copy non-primitive types passed into functions, but treats them as refences. No additional information is stored in this recursive implementation. The function stack does grow as it recurses deeper, but it does so independently of *n*. Hence, the worst case scenario of this implementation's space complexity is ***O(1)***.