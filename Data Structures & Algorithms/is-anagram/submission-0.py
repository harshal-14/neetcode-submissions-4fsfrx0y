class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use 2 dicts to store key:val pair as alphabet:frequency for s and t
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False
        #iterate thru s and t to add elements in countS and countT
        for i in s:
            countS[i] = countS.get(i, 0) + 1
        # if countS == countT return True else False
        for j in t:
            countT[j] = countT.get(j, 0) + 1

        if countS==countT:
            return True
        else: return False

        