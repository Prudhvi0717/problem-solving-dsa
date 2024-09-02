## link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    We need to find `lowest` common ancestor i.e according to depth not value of node.
    So we just need to find a node which value lies between the given p and q vals (inclusive)
    It would be the common ancestor to both p and q nodes.

    steps:
    1. If cur node value is greater than p and q vals then we need to search left sub tree
        because all the right subtree nodes have values > cur node
    2. If cur node value is less than p and q vals then we need to search right subtree
        because all the left subtree nodes haves values < cur node.
    3. The else situation is which satisfies teh condition p.val <= cur.val <= q.val
        so it will be the result node.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root