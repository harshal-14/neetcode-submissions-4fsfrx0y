# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")# dfs
        def getMax(node):
            # helper function to get max of path
            nonlocal res
            if not node:
                return 0

            # "What can my left child offer me going downward?"    
            left_path = max(getMax(node.left),0)

            # "What can my right child offer me going downward?"
            right_path = max(getMax(node.right),0)

            # "If I'm the peak of an arch, how good is it?"
            res = max(res, node.val + left_path + right_path)

            # "What's the best single branch I offer MY parent?"
            return node.val + max(left_path, right_path)
        getMax(root)

        return res

        