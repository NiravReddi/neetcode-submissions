class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zcount=nums.count(0)
        if zcount>=2:
            return [0]*len(nums)
        elif zcount==1:
            prefix=1
            r=[]
            l=0
            for i in nums:
                if i==0:
                    r.extend([0]*l)
                    l=0
                    continue
                l+=1
                prefix*=i
            r.append(prefix)
            r.extend([0]*l)
            return r
        else:
            
            prefix=1
            r=[]
            for i in range(0,len(nums)):
                prefix*=nums[i]
            for j in range(0,len(nums)):
                r.append(prefix//nums[j])
            return r

        
        