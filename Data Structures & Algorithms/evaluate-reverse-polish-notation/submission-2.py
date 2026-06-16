class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+*-/":
                stack.append(int(i))
            elif i=="+":
                stack.append(stack.pop()+stack.pop())
            elif i=="-":
                a1=stack.pop()
                a2=stack.pop()
                stack.append(a2-a1)
            elif i=="*":
                stack.append(stack.pop()*stack.pop())
            else:
                a1=stack.pop()
                a2=stack.pop()
                stack.append(int(a2/a1))
        return stack[0]