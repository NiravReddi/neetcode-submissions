class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=defaultdict(list)
        for i in nums:
            ans[i].append(1)
        freq=defaultdict(list)
        for i in ans.keys():
            freq[len(ans[i])].append(i)
        res=[]
        sf=sorted(list(freq.keys()),reverse=True)
        while(k>0):
            res.append(freq[sf[0]].pop(0))
            if len(freq[sf[0]])==0:
                sf.pop(0)
            k-=1
        return res
            