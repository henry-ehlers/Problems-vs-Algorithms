# HTTRPRouter using a Trie

## Time Complexity
Similar to the trie implemented earlier, the worst case scenario for insertions and look-ups is ***O(n)***, where *n* is the number of sub-paths the trie must traverse to either store or find a handler. 

## Space Complexity
Again, similar to the previous trie, the worst case scenario is no overlap between any of the (sub) paths that need to be stored, so we must store a node for every subpath we encounter. This means the wost case space complexity is also ***O(n)***, where *n* is the number of unique subpaths encountered.