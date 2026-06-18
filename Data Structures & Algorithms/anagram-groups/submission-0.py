class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord("a")]+=1
            if tuple(count) not in res:
                res[tuple(count)]=[i]
            else:
                res[tuple(count)].append(i)
        return list(res.values())