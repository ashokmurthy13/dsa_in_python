class TrieNode:
    def __init__(self, letter=''):
        self.children = [None] * 26
        self.isLeaf = False
        self.letter = letter

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> bool:
        current = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
            current = current.children[index]
        current.isLeaf = True
        return True
    
    def search(self, word:str) -> bool:
        current = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            if current.children[index] is None:
                return False
            else:
                current = current.children[index]
        
        if current.isLeaf:
            return True
        else:
            return False
        
    def start_with(self, prefix:str) -> bool:
        pass


class Test:

    def test_trie(self):
        trie = Trie()

        words = ["the", "their","them","money","mouse","mousepad"]

        for word in words:
            trie.insert(word)

        print(trie.search("the"))
        print(trie.search("mouse"))
        print(trie.search("them"))

test = Test()
test.test_trie()