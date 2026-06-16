class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            leftlen=len(left)
            rightlen=len(right)
            r=0
            l=0
            ret=[0]*(leftlen+rightlen)
            ind=0
            while(l<leftlen and r<rightlen):
                if left[l]<=right[r]:
                    ret[ind]=left[l]
                    l+=1
                else:
                    ret[ind]=right[r]
                    r+=1
                ind+=1
            while(l<leftlen):
                ret[ind]=left[l]
                l+=1
                ind+=1
            while(r<rightlen):
                ret[ind]=right[r]
                r+=1
                ind+=1
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

        