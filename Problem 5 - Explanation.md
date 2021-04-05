# Autocomplete with Tries

## Time Complexity

**Find** / **Suffixes**
The worst case scenario is an input prefix of minimal length (i.e. 1), and all stored words in the trie share no common letters. In such a case all *n* nodes in the Trie would need to visited to find all words / suffixes, resulting in a worst case scenario of ***O(n)***.

**Insert**
Again, the worst case scenario is a complete non-overlap between letters already in the Trie and letters in the input words. In such a case, every insertion of a word of length *n* would require *n* new nodes to be created and added to the Trie. Such insertion would require *n* insertion function calls, resulting in a worst case scenario of ***O(n)***.


## Space Complexity

**Find** / **Suffixes**
The find operation does not store additional information and does not add meaningfully to the function stack. As a result, the wost case space complexity is ***O(1)***.

**Insert**
In the wost case scenario, there is a complete non-overlap between words stored in the Trie already and any word added to it. As such, a word of length *n*, would require *n* new nodes to be created and stored in memory resulting in a worst case space complexity of ***O(n)***.