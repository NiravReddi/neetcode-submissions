class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def ispermute(s1,s2):
            print(s1,s2)
            dic1=defaultdict(int)
            dic2=defaultdict(int)
            for i in s1:
                dic1[i]+=1
            for j in s2:
                dic2[j]+=1
            if dic1==dic2:
                return True
            return False
        dic=defaultdict(int)
        if len(s1)<len(s2):
            for i in s1:
                dic[i]+=1
            for j in range(len(s2)-len(s1)+1):
                if s2[j] in dic.keys():
                    if ispermute(s2[j:j+len(s1)],s1):
                        return True
                    if ispermute(s2[j-len(s1)+1:j+1],s1):
                        return True
        else:
            for i in s2:
                dic[i]+=1
            for j in range(len(s1)-len(s2)+1):
                if s1[j] in dic.keys():
                    if ispermute(s1[j:j+len(s1)],s2):
                        return True
                    if ispermute(s1[j-len(s1)+1:j+1],s2):
                        return True
        return False