class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        if a!=0:
            heapq.heappush(heap,(-a,'a'))
        if b!=0:
            heapq.heappush(heap,(-b,'b'))
        if c!=0:
            heapq.heappush(heap,(-c,'c'))
        res=""
        while(heap):
            count,letter=heapq.heappop(heap)
            count=-count
            if res=="":
                res=letter
                count-=1
                if count!=0:
                    heapq.heappush(heap,(-count,letter))
            else:
                if len(res)>=2 and (res[-1]==letter and res[-2]==letter):
                    
                    if heap:
                        count1,letter1=heapq.heappop(heap)
                        count1=-count1
                        count1-=1
                        res+=letter1
                        if count1!=0:
                            heapq.heappush(heap,(-count1,letter1))
                        heapq.heappush(heap,(-count,letter))
                    else:
                        return res
                else:
                    res+=letter
                    count-=1
                    if count!=0:
                        heapq.heappush(heap,(-count,letter))
        return res