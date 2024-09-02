## link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        
        We know that preorder is Root Left Right and inorder is Left Root Right.
        The first element of the preorder traveral is the root.
        And by finding where this root is in inorder arr, we know that elements to left 
        of root in inorder are part of left subtree and elements to the right belongs to 
        right subtree.
        For Eg: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        root = 3, in inorder [9] 3 [15,20,7]
        9 belongs to left subtree and 15,20,7 belongs to right.
        Now in preorder arr we can partition it into two parts, excluding root i.e [9] [20 15 7]
        based on inorder arr parts len.
        So we recursively create subtrees by passing the partitioned arrays.
        """

        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


