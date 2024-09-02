## link: https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        A BST is valid if,
        all the vals of nodes in the left subtree are less than current node value 
        i.e -inf <= left-node-vals <= curnode.val

        all the vals of nodes in the right subtree are greater than current node value
        i.e curnode.val <= right-node-vals <= inf 

        So we will set two variables called leftMin and rightMax to -inf and inf
        for left subtree rightMax is changed to curNode val, such that -inf <= left nodes <= cur.val

        for right subtree leftMin is changed to curNode val, such that cur.val <= right nodes <= inf.
        We recursively check for all nodes by changing the leftMin and rightMax accordingly.
        """
        def valid(node, leftMin, rightMax):
            if not node:
                return True
            if not (node.val < rightMax and node.val > leftMin):
                return False
            
            return valid(node.left, leftMin, node.val) and valid(node.right, node.val, rightMax)
        
        return valid(root, float("-inf"), float("inf"))