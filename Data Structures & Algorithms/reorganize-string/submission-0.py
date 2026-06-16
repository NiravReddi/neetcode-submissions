class Solution:
    def reorganizeString(self, s: str) -> str:
        res=""
        hash=[]
        dic=defaultdict(int)
        for i in s:
            dic[i]+=1
        for i in dic.keys():
            heapq.heappush(hash,(-dic[i],i))
        while(len(res)!= len(s) and hash):
            freq,i=heapq.heappop(hash)
            freq=-freq
            if res=="":
                res=i
                freq-=1
                if freq!=0:
                    heapq.heappush(hash,(-freq,i))
            else:
                if res[-1]!=i:
                    res+=i
                    freq-=1
                    if freq!=0:
                        heapq.heappush(hash,(-freq,i))
                else:
                    if not hash:
                        return ""
                    else:
                        freq1,i1=heapq.heappop(hash)
                        res+=i1
                        freq1=-freq1
                        freq1-=1
                        if freq1!=0:
                            heapq.heappush(hash,(-freq1,i1))
                        heapq.heappush(hash,(-freq,i))
        return res
