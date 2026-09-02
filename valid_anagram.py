# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs={}
        ct={}
        for i in s:
            cs[i] = cs.get(i,0)+1  # Used for getting value of occurence of the each character in dictionary
        for i in t:
            ct[i] = ct.get(i,0)+1

        yes = 0
        if len(s) == len(t) and cs == ct: # The anagram is the word with same length and character, but only with different order
            for i in s:
                if i in t:
                    yes = 1
                else:
                    yes = 0
                    break     # If any 1 character not in t means then it is not anagram.
        if yes == 1:
            return True
        else:
            return False





            

        
