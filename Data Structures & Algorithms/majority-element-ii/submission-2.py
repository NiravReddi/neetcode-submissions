class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nbythree=len(nums)//3
        dic=defaultdict(int)
        res=[]
        for i in nums:
            dic[i]+=1
            if dic[i]>nbythree and i not in res:
                res.append(i)
        return res

        