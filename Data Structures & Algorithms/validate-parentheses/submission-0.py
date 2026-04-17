from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        #approach: maintian a map of key val pairs
        # The key insight: opening brackets get pushed. When you see a closing bracket, 
        #pop the top and verify it's the matching opener. If the stack is empty at the end, everything matched.
        hashmap = {"[" : "]",
                    "{" : "}",
                    "(" : ")"}
        
        stack = deque()
        # iterate thru s 
        for char in s:
            #push new opening bracket elements onto the stack
            if char in hashmap:
                stack.append(char) 
            else:
                if not stack or hashmap[stack.pop()] != char:
                    return False
        
        return len(stack)==0