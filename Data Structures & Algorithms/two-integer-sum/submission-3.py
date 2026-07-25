class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     # nums[0] + nums[1] = 7
     # nums[j] = target - nums[i]
     # return [i,j]
        seen = {}
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff],i]
            seen[num] = i