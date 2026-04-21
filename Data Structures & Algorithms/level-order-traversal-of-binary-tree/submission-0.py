# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resqueue = deque() # init
        res = []

        resqueue.append(root) # init res with root node

        while resqueue: # run till queue is not empty
            qLen = len(resqueue) # iterate thru one level at a time
            level = [] #adding them to their own list

            for i in range(qLen): # loop every val in this queue
                node = resqueue.popleft()        #pop the elements
                if node:
                    level.append(node.val)
                    resqueue.append(node.left)
                    resqueue.append(node.right)

            if level:    
                res.append(level)

        return res


                
        

        

        
