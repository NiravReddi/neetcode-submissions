class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        curr=""
        for i in path:
            if i=='/' and curr=='':
                continue
            elif i=='/' and curr!='':
                if curr=="..":
                    if stack:
                        stack.pop()
                        curr=""
                    else:
                        curr=''
                elif curr==".":
                    curr=""
                else:
                    stack.append(curr)
                    curr=''
            else:
                curr+=i
        if curr=="..":
            stack.pop()
        elif curr!="." and curr!="":
            stack.append(curr)
        print(stack)
        return "/"+"/".join(stack)