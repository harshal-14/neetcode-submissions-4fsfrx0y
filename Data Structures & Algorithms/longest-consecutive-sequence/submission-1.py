class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach:
        # use a hashset such that it doesnt do double counting and for O(1) lookup
        # We need the starting point such that if n-1 exists then its not a starting point
        # if n-1 doesnt exist iterate along hashset continue streak until next element exists
        # if doesnt exist go to next element
        
        hashset = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in hashset:
                length = 1
                while (num+length) in hashset:
                    length +=1
                longest = max(length, longest)
        return longest
                
                