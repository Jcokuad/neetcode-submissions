class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #Python List
        closeToOpen = { ")": "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen: # Checks for closing parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False # Goal is for stack to be empty 
        # Shows that all bracket pair have been found and removed

        