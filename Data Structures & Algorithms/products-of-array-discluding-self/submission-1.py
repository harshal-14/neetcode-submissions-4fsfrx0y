class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        prefix = 1
        postfix = 1

        for num in range(n):
            res[num] *=prefix
            prefix *= nums[num]
        
        for num in range(n-1, -1, -1):
            res[num] *=postfix
            postfix *=nums[num]
        return res
        


