class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq.keys():
                freq[i]+=1
            else:
                freq[i]=1
        val={}
        for i in freq.keys():
            if freq[i] in val.keys():
                val[freq[i]].append(i)
            else:
                val[freq[i]]=[i]
        res=[]
        for i in sorted(val.keys(),reverse=True):
            res.extend(val[i])
            if len(res)>=k:
                break
        return res[:k]