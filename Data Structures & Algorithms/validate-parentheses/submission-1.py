class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for char in s:
            # ( ) 
            if char in mapping:
                match = mapping[char] # ) -> ( 
                # ( == (
                if stack and stack[-1] == match:
                    stack.pop() # remove (
                else:
                    return False
            else:
                # ( is appended to the stack
                stack.append(char)
        return not stack