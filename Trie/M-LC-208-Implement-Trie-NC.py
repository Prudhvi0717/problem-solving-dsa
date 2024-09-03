## link: https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.endOfWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                return False
            curNode = curNode.children[letter]
        return curNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for letter in prefix:
            if letter not in curNode.children:
                return False
            curNode = curNode.children[letter]
        return True
