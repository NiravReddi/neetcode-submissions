class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=sorted(list(zip(position,speed)),reverse=True)
        stack=[]
        for i in fleet:
            chd=(target-i[0])/i[1]
            print(chd)
            if stack and chd<=stack[-1]:
                continue
            else:
                stack.append(chd)
        return len(stack)
