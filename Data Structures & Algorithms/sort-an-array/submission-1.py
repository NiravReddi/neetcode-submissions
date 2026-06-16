class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            ret=[0 for i in range(len(left)+len(right)) ]
            i=0
            l=0
            r=0
            while(l<len(left) and r<len(right)):
                if left[l]<right[r]:
                    ret[i]=left[l]
                    l+=1
                else:
                    ret[i]=right[r]
                    r+=1
                i+=1
            while(l<len(left)):
                ret[i]=left[l]
                i+=1
                l+=1
            while(r<len(right)):
                ret[i]=right[r]
                r+=1
                i+=1
            
            return ret
        def mergesort(arr):
            if len(arr)>1:
                mid=len(arr)//2
                left=mergesort(arr[:mid])
                right=mergesort(arr[mid:])
                ret=merge(left,right)
                return ret
            return arr
        return mergesort(nums)