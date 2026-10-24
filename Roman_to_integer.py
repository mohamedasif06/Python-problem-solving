class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        cv=0
        for i in range(len(s)):
            if i+1 < len(s) and d[s[i]]<d[s[i+1]]:
                cv -= d[s[i]]
            else:
                cv += d[s[i]]
        return cv
