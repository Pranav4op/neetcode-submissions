class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        j = 0
        c = 0
        while (j != len(t)) and (i != len(s)):
            if s[i] == t[j]:
                c += 1
                i += 1
            j += 1
        return c == len(s)