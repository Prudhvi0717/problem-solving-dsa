## link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    We can use preorder traveral of the tree with null nodes are represented by "N"s
    as the serialized string.
    This helps us in recreating the tree recursively just by following the 
    Root Left Right order.

    1. We create, root node
    2. create left nodes to subsequent nodes until we reach N
    3. then create right node and recurse from step 1

    this recursive approach recreates tree from the preorder traversal.
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        data = []

        def dfs(root):
            if not root: 
                data.append("N")
                return

            data.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N": 
                self.inc()
                return None

            node = TreeNode(int(vals[self.i]))
            self.inc()
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

    def inc(self):
        self.i += 1

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))