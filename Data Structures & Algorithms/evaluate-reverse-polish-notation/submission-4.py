class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "*+-/":
                stack.append(int(i))
            elif i=='+':
                stack.append(stack.pop()+stack.pop())
            elif i=='-':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2-op1)
            elif i=='*':
                stack.append(stack.pop()*stack.pop())
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(int(op2/op1))
        return stack[0]