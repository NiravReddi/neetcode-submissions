class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        l=0
        for i in s:
            if i in "{[(":
                stack.append(i)
                l+=1
            elif i=='}':
                if len(stack)> 0 and stack[l-1]=='{':
                    stack.pop(l-1)
                    l-=1
                else:
                    return False
            elif i==')':
                if len(stack)> 0 and stack[l-1]=='(':
                    stack.pop(l-1)
                    l-=1
                else:
                    return False
            elif i==']':
                if len(stack)> 0 and stack[l-1]=='[':
                    stack.pop(l-1)
                    l-=1
                else:
                    return False
        if len(stack)>0:
            return False
        return True
            
        