class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()

        l = 0
        r = 1

        if len(s) == 0: return 0 

        res = 0
        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l+=1
            subset.add(s[r])
            res = max(res, r - l + 1)
        return max(res, r-l+1)