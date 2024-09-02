## link: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    The intuition is to use bottom up approach.
    At each node we calculate,
    1. leftPathSum(without split)
    2. rightPathSum(without split)
    3. sum of leftPathSum(without split) + root + rightPathSum(without split)

    So that we could have max of non split sum of linear nodes of left and right of a node.
    And the sum of them with cur node to form a subtree sum.

    We update max as we go up and return the max sum found so far.
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = [root.val]
        def maxPathSumHelper(root):
            if not root:
                return 0

            leftPathSum = max(maxPathSumHelper(root.left), 0)
            rightPathSum = max(maxPathSumHelper(root.right), 0)

            subTreeSum = leftPathSum + root.val + rightPathSum
            pathSum = root.val + max(leftPathSum, rightPathSum)
            maxPathSum[0] = max(maxPathSum[0], subTreeSum, pathSum)

            return pathSum

        maxPathSumHelper(root)
        return maxPathSum[0]