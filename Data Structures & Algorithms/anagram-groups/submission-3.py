class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = defaultdict(list)
        # key: val pair is frequency of char: [list of words from strs that fulfil this frequency count]
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] +=1
                #count[1,0,0,0,0,....]
            res[tuple(count)].append(s)
        return list(res.values())
            