class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # init set
        seen = set()
        # iterate thru array to add elements to hash table
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False