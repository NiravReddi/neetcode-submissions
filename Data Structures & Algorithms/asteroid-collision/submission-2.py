class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if i>0:
                stack.append(i)
            else:
                if stack and abs(i)==stack[-1] and stack[-1]>0:
                    stack.pop()
                    continue
                else:
                    while(stack and abs(i)>stack[-1] and stack[-1]>0):
                        stack.pop()
                    if stack and abs(i)==stack[-1] and stack[-1]>0:
                        stack.pop()
                        continue
                    if stack and abs(i)<stack[-1] and stack[-1]>0:
                        continue
                    stack.append(i)
        return stack
                