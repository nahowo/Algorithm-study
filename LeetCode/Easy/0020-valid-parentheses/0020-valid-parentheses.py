class Solution:
    def isValid(self, s: str) -> bool:
        stack=[""]
        for i in s:
            if stack[-1]=="(" and i==")" or stack[-1]=="{" and i=="}" or stack[-1]=="[" and i=="]":
                stack.pop()
            else:
                stack.append(i)
        if len(stack)==1:
            return True
        else:
            return False