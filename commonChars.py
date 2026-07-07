from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0]) #Used to find the frequency of characters
        for word in words[1:]:
            common = common & Counter(word) #Keeps only the characters that are common in both dictionaries
        ans=[]
        for ch in common:
            ans.extend([ch]*common[ch]) #If a character appeared more than 1 time. Then it should return the duplicate also
        return ans
