from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create n buckets 1 to n
        # buckets = [[] for _ in range(n)]

        seen = {}
        counts = Counter(nums)
        # group nos based on their frequencies
        for num, freq in counts.items():
            seen.setdefault(freq, []).append(num)

        # pick top k nos from buckets starting n to 1
        res = []
        for i in range(len(nums), 0, -1):
            if i in seen:
                for num in seen[i]:
                    res.append(num)
                    if len(res)==k:
                        return res
