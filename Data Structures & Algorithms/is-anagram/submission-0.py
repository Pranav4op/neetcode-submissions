from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map=defaultdict(list)
        if len(t)==len(s):
            sorted_s=tuple(sorted(s))
            sorted_t=tuple(sorted(t))
            map[sorted_s]=sorted_t
            if sorted_t in map:
                return True
            else:
                return False
        else:
            return False