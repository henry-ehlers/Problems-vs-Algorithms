# HTTRPRouter using a Trie

## Time Complexity

**Lookup**
The worst case scenario of the lookup operation's time complexity is **O(n)**, where *n* is the number of subpaths in the path provided. This scenario comes true if all *n* subpaths are present and must hence be traversed in order to locate the handler of this particular path.

**Add Handler**
The add-handler's worst-case scenario's time complexity is **O(n)**, where *n* is the number of subpaths in the provided path. This is the case simply because this implementation must traverse all *n* subpaths in order to ultimately insert a handler to the tail of the provided path.

## Space Complexity

**Lookup**
The lookup method stores no additional information, and does not meaningfully add to the function stack. As a result, the worst case scenario of the lookup method's space complexity is **O(1)**.

**Add Handler**
The add handler's worst case scenario (in terms of space complexity) comes true when there is no overlap between the subpaths already stored in the Trie and the subpaths in the path to be added. In such a case, each of the *n* input subpaths must be added to the Trie in the form of a node, resuling in a wost-case space complexity of **O(n)**.