class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        dic=defaultdict(int)
        for i in triplets:
            if i[0]>target[0] or i[1]>target[1] or i[2]>target[2]:
                continue
            else:
                ind=0
                for j in i:
                    if j==target[ind]:
                        dic[ind]=j
                    ind+=1
        if len(dic.keys())==3:
            return True
        return False
