from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s: 
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ")" and stack[-1] == '(':
                    stack.pop()
                elif char == "}" and stack[-1] == '{':
                    stack.pop()
                elif char == "]" and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
        if stack:
            return False
        return True