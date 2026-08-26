class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for letter in columnTitle:
            value = ord(letter) - ord('A')+1 
            #using ord() for converting letter into it's ASCII value
            result = result * 26 + value #formula
        return result 

# normal decimal number, we use:

# result = result × 10 + digit

# Excel column system is essentially a base-26 system, so

# result = result × 26 + value
