class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(n):
            if haystack[i:i+n] == needle:
                return i
        return -1
