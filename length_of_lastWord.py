class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = " ".join(s.split()) 
        #Use .split() combined with .join() to reduce multiple consecutive spaces into a single space, while also trimming the ends.
        words = words.split(" ") #Putting all the words into a list
        return len(words[-1])
        
