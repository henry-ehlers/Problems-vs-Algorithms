# Autocomplete with Tries

## Time Complexity
The time complexity for a look-up or an inseertion is ***O(n)***, as it must traverse as many nodes as there are are characters *n* in the input.

## Space Complexity
In the worst case scenario, every newly added word is completely unique from all previous ones, meaning we must add as many new nodes as there are letters in the word. Hence, the worst case space complexity is ***O(n)***.