class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        for c in s:
            if c.isalnum():
                strs += c.lower()
        if strs == strs[::-1]:
            return True
        return False
