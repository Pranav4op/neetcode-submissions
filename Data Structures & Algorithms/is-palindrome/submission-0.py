class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for i in s:
            if i.isalnum():
                a += i
        a = a.strip().lower()

        if a[::-1] == a:
            return True
        else:
            return False