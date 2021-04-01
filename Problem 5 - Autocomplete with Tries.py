from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self, word_end = False):
        assert(isinstance(word_end, bool))
        self.word_end = word_end
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = "") :
        found_suffixes = []
        for letter in self.children.keys():
            #print("suffix letter: {}".format(letter))
            new_suffix = suffix + letter
            #print(new_suffix)
            if self.children[letter].word_end:
                #print("WORD END")
                found_suffixes.append(new_suffix)
            found_suffixes.extend(self.children[letter].suffixes(suffix=new_suffix))
        #print(found_suffixes)
        return found_suffixes

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.insert(letter)
            current_node = current_node.children[letter]
        current_node.word_end = True
            
    def find(self, prefix):
        current_node = self.root
        for letter in prefix:
            #print("prefix letter: {}".format(letter))
            if letter in current_node.children:
                #print("present")
                current_node = current_node.children[letter]
            else:
                return None
        return current_node
            
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

node = MyTrie.find("an")
print(node.suffixes())
