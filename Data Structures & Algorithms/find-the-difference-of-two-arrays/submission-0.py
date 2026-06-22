class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # logic is use set
        arr1 = set(nums1)
        arr2 = set(nums2)
        res1, res2 = [], []

        for n in arr1:
            if n not in arr2:
                res1.append(n)
        for n in arr2:
            if n not in arr1:
                res2.append(n)
        

        return [res1, res2]

