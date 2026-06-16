class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "[{(":
                stack.append(i)
            if i==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            if i=='}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            if i==')':
                if stack and  stack[-1]=='(':
                    stack.pop()
                else:
                    return False
        return len(stack)==0