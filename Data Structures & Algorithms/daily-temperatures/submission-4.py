class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while(stack and stack[-1][0]<temperatures[i]):
                lastval,lastind=stack.pop()
                res[lastind]=i-lastind
            stack.append((temperatures[i],i))
            
        return res
            

