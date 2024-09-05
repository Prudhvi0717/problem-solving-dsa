## link: https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    """
    create copy nodes and recursively create the children and append them to
    parent node during callback.

    Keep a map for old to new nodes to not recreate nodes for common neighbors.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for c in node.neighbors:
                copy.neighbors.append(dfs(c))

            return copy

        return dfs(node) if node else None