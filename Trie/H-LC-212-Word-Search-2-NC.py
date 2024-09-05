## link : https://leetcode.com/problems/word-search-ii/description/

"""
To search for all words in boards that are in given list, we need to search for each word
in the board with backtracking. But it would be very inefficient solution.

So we create a Trie with all the given list of words.
Such that we could traverse over the boards check if any of words in trie has this letter as start.
If exists we recursively search for the prefixes in board starting from that letter.

So we have a letter A and we start by checking if it exists in Trie if it exists we recurse
further to check next neighbours and parallely check if there are words with these prefix.
If there are none then stop.

Like this we will find all words with those prefix path.
"""

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
            cur.refs += 1
        cur.endOfWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def isValidCell(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, node, word):
            if (
                not isValidCell(r, c) or 
                board[r][c] not in node.children or
                node.children[board[r][c]].refs < 1 or
                (r, c) in visit
            ):
                return

            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
                node.endOfWord = False
                root.removeWord(word)
            visit.add((r, c))

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)