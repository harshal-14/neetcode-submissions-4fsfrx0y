# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        # recursive approach
        # maxLen = 0
        # leftDepth = self.maxDepth(root.left)
        # rightDepth = self.maxDepth(root.right)

        # return 1 + max(leftDepth, rightDepth)

        #iterative approach
        stackio = [[root,1]]
        maxdepth = 0
        while stackio:
            node, depth = stackio.pop()

            if node:
                maxdepth = max(maxdepth, depth)
                stackio.append([node.left, depth+1])
                stackio.append([node.right, depth +1])
        
        return maxdepth