"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtoNew = {} # hashmap for mapping old to new

        def clone(node):
            if node in oldtoNew:
                return oldtoNew[node]

            graphnode = Node(node.val) #val of original node
            oldtoNew[node] = graphnode #also add this to new hashmap mapping
            for nei in node.neighbors:
                graphnode.neighbors.append(clone(nei))
            return graphnode

        return clone(node) if node else None
