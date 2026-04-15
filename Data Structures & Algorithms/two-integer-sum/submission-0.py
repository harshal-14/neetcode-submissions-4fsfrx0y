class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate thru nums if diff = target - nums[i] exists in hashmap 
        counts = {}
        for i, num in enumerate(nums): #i = idx and num = val
            diff = target - num

            if diff in counts: 
                return[counts[diff], i]
            else:
                counts[num] = i
                


                
                