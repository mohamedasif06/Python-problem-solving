# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_to_char = {}
        s = s.split(" ")
        p_len = len(pattern)
        s_len = len(s)
        if p_len != s_len:
            return False
        for i in range(s_len):
            ch = pattern[i]
            word = s[i]

            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False

            char_to_word[ch] = word
            word_to_char[word] = ch
        return True
