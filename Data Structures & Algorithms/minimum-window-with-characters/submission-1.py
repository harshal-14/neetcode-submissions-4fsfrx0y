from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:                          # 1. "t is None" misses empty string
            return ""

        #2 hashmaps to store count of each char of s and t
        t_count = {}
        window = {}

        # update the hashmap for t with chars and their frequency of occurence
        for count in t:
            t_count[count] = 1 + t_count.get(count, 0)

        # init haves(len of freq in c) and needs(len)
        have, need = 0, len(t_count)

        l = 0
        res = [-1, -1]
        reslen = float("infinity")

        # iterate thru s
        for r in range(len(s)):
            c = s[r] ##?
            window[c] = 1 + window.get(c, 0)

            # if our freq of chars we care abt from t matches increment haves
            if  c in t_count and window[c] == t_count[c]:
                have +=1
            
            # try reducing length of window
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l +1

                window[s[l]] -= 1

                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l+=1
        l , r = res
        return s[l:r +1] if reslen != float("infinity") else ""