class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic=defaultdict(int)
        for i in bills:
            if i-5>0:
                isub=i-5
                if (isub//10)<=dic[10]:
                    dic[10]-=(isub//10)
                    isub-=((isub//10)*10)
                if (isub//5)<=dic[5]:
                    dic[5]-=(isub//5)
                    isub-=((isub//5)*5)
                
                if isub>0:
                    return False
                dic[i]+=1
            else:
                dic[i]+=1
        return True