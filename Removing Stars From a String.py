class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        l = 0
        while l != len(s):
            if s[l] != "*":
                stack.append(s[l])
            else:
                stack.pop()
            l += 1
        
        return "".join(stack)
