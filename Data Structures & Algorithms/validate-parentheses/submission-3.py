class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ctoo = {']' : '[' , '}' : '{' , ')' : '('}
        for c in s:
            if c in ctoo:
                if stack and stack[-1] == ctoo[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False