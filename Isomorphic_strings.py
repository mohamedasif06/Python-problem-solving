class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a in d1 and d1[a]!=b:
                return False
            if b in d2 and d2[b]!=a:
                return False
            d1[a]=b
            d2[b]=a
        return True
        
                

