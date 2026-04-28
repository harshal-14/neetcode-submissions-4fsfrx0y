class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def traverse(i, curlist, total):
            if total == target:
                res.append(curlist.copy())
                return

            if i>=len(nums) or total > target:
                return

            curlist.append(nums[i])
            traverse(i, curlist, total + nums[i])
            curlist.pop()
            traverse(i + 1, curlist, total)

        traverse(0, [], 0)
        return res
            
            

