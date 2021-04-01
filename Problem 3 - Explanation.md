# Rearrange Array Elements

## Time Complexity
The most computationally challenging aspect of this implementation is the recursive merge sort. Merge sort, in its worst case scenario, has a time complexity of ***O(n.log2(n))***, as it halves the possibility space, but may need to to do *n* times.

## Space Complexity
Merge sort does not sort *in-place*, but instead creates copies of the (sub-)lists of interest. Subsequently, the larger the input list, the larger and more plentiful the number of stored object as a function of the size *n* of the input list. Subsequently the space complexity is ***O(n)***.