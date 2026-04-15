class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers such that i at start j at end
        # increment i+1 and decrement j-1 if i+1 = j-1 
        # continue till end i=j break if False

        i = 0
        j = len(s) - 1

        while i<j:
            
            # skip alphanumeric chars
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

