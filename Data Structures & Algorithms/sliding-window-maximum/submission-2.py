import bisect
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        heap=[]
        for i in range(k):
            dic[nums[i]]+=1
            if dic[nums[i]]==1:
                bisect.insort(heap,nums[i])
        print(heap)
        res=[heap[-1]]
        l=0
        for r in range(k,len(nums)):
            dic[nums[r]]+=1
            if dic[nums[r]]==1:
                bisect.insort(heap,nums[r])
            dic[nums[l]]-=1
            if dic[nums[l]]==0 :
                del dic[nums[l]]
                
                heap.remove(nums[l])
            print(dic)
            res.append(heap[-1])
            l+=1
        return res
            