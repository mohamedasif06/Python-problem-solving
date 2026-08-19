class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n+1): #we want to check every position where needle can possibly fit inside haystack.
            if haystack[i:i+n] == needle:
                return i
        return -1
