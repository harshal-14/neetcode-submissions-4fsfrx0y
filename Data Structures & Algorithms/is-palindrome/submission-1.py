class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        result = "".join([char.lower() for char in s if char.isalnum()])
        j = len(result) - 1
        for letter in range(len(result)):
            if result[letter]!=result[j]:
                return False
            j-=1
        return True
