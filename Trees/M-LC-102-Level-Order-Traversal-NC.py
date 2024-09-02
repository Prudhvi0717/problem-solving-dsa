## link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    To get the level order traversal of binary tree, we just need to perform BFS
    But it should be in such a way that all nodes of same level are processed at once or in groups.
    So we use a queue to store nodes and while - for combination to pull out all nodes of same level in 
    one go. This technique is helpful in all kinds of trees and graph questions where we need to process
    The nodes in groups of level and adjacency.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node: 
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level: res.append(level)
        return res

