class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack: # Checks whether the list is empty
                    return False
                if stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0


        
