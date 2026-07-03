class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            punct = "!?',;."
            for ch in punct:
                paragraph = paragraph.replace(ch," ")
                #Replaces the current punctuation character with a space.
                #Stores the modified string back into paragraph.
            paragraph = paragraph.lower().split() # -> split(): Splits on any whitespace (spaces, tabs, newlines)
            wc = {}
            for i in paragraph:
                if i in wc:
                    wc[i] += 1
                    #If the word already exists, increase its count by 1.
                else:
                    wc[i] = 1
            for i in banned:
                if i in wc:
                    del wc[i] #Removes the word if it is banned
            return max(wc,key=wc.get) # Returns the key the has maximum value
