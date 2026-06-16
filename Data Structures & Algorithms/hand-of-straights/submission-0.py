class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic=defaultdict(int)
        for i in hand:
            dic[i]+=1
        while(len(dic)!=0):
            mx=max(dic.keys())
            
            for i in range(groupSize):
                if mx-i not in dic.keys():
                    return False
                else:
                    
                    dic[mx-i]-=1
                    if dic[mx-i]==0:
                        del dic[mx-i]
        
        return True