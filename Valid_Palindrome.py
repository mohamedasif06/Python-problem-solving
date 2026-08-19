import re
class Solution:
    def isPalindrome(self, s):
        cleaned_text = (re.sub(r'[^a-zA-Z0-9]','',s)).lower()
      # re.sub(r'[^a-zA-Z0-9] using this because for replacing all non-alphanumeric characters with nothing and making into lowercase
        rev = cleaned_text[::-1] # String is reveresed
        if rev == cleaned_text:
            return True
        else:
            return False
