# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ""

        while columnNumber > 0:
            # Excel uses 1-26, but Python indexes from 0-25
            columnNumber -= 1

            # % 26 gives a value from 0 to 25
            # This value is used as the index for A-Z
            rem = columnNumber % 26

            # Add the corresponding letter to the result
            result += letters[rem]

            # Move to the next position
            columnNumber //= 26

        # Letters are found from right to left, so reverse them
        return result[::-1]
