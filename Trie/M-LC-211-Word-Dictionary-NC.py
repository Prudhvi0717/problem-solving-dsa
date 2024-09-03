## link: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    """
    To match a "." with any letter, we need to consider all the children as valid.
    Which implies that we need search for the next letter of the word in all of these children.
    So we loop over all the children and recursively call the same function on remaining word 
    with each child as source.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.root

        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.endOfWord = True

    def smallSearch(self, curNode: TrieNode, word: str) -> bool:

        for i in range(len(word)):
            if word[i] == ".":
                for n in curNode.children:
                    if self.smallSearch(curNode.children[n], word[i + 1:]):
                        return True
                return False
            if word[i] not in curNode.children:
                return False
            curNode = curNode.children[word[i]]
        return curNode.endOfWord

    def search(self, word: str) -> bool:
        return self.smallSearch(self.root, word)
