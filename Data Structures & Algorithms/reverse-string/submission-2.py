class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        temp = None
        for letter in range(len(s)//2):
            temp = s[letter]
            s[letter] = s[j]
            s[j] = temp
            j-=1
