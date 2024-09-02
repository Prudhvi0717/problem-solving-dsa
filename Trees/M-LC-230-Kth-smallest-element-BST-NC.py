## link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    The intuition is to simple traverse the BST in order and count each root occurence.
    increase a counter to track number of elements processed (ascending order) and return the kth element.
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## recursive solution

        # self.ans, self.cnt = None, 0
        # def inOrderTraveral(root):
        #     if self.ans or not root: return
            
        #     inOrderTraveral(root.left)
        #     self.cnt += 1
        #     if self.cnt == k: self.ans = root.val
        #     inOrderTraveral(root.right)

        # inOrderTraveral(root)
        # return self.ans


        ## iterative solution
        stack = []
        cur = root
        cnt = 0

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            cnt += 1
            if cnt == k: return cur.val

            cur = cur.right
