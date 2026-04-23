# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = None
        # dfs using recursion
        # base case:
        def dfs(node):
            nonlocal cnt, res

            if not node or res is not None:
                # result found exit early
                return

            dfs(node.left)
            
            cnt -=1 # visited the node decrement count
            if cnt==0:
                res = node.val
                return
            dfs(node.right)

        dfs(root)

        return res

        
