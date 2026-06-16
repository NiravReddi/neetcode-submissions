class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        ln=len(nums)//3
        res=[]
        for i in nums:
            if i in dic.keys():
                dic[i]+=1 
            else:
                dic[i]=1
            if dic[i] >ln and i not in res:
                res.append(i)
        return res