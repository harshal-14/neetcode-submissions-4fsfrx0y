class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countt, counts = {}, {}
        if len(s) != len(t):
            return False
        for i in t:
            countt[i] = 1 + countt.get(i,0)
        print(countt)
        for j in s:
            counts[j] = 1 + counts.get(j, 0)
        print(counts)
        if countt == counts:
            return True
        else: 
            return False
