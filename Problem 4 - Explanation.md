# The Dutch National Flag Problem

## Time Complexity
The worst-case time complexity of this implementation is also its best and average complexity, namely ***O(n)***. This is because it must iterate over all *n* elements of the input list in order to count the number of *0*, *1*, and *2* elements, in order to subsequently create the new output list (constant time, and hence ignored here).

## Space Complexity
This implementation does not recurse, but does create a copy of the input list. Hence, it's complexity increases as the input list grows, meaning its space complexity is ***O(n)***.