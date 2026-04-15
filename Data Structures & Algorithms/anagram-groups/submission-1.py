class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # why default dict? because normal dict throws KeyError when trying to append

        for s in strs: # iterate thru strs
            count = [0] * 26 # empty array of size 26

            for c in s: # iterate thru each string in strs
                count[ord(c) - ord("a")] += 1 # ascii val normalization

            res[tuple(count)].append(s) # ?? append to res dict but why tuple? so immutable

        return list(res.values()) # what is value?