class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode the string using length first then special character for delimiter
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        decoded_res = []
        # idx = 0
        i = 0
        #iterate over length of s
        while i < len(s):
            # use pointer j to keep one point ahead to find length of word
            j = i
            while s[j] != "#": # keep going until you hit #
                j += 1 # when you hit # the i:j is your length
            
            length = int(s[i:j])
            decoded_res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        
        return decoded_res