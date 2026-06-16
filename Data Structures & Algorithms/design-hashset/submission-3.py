import bisect
class MyHashSet:

    def __init__(self):
        self.arr=[]
        

    def add(self, key: int) -> None:
        ind=bisect.bisect_left(self.arr,key)
        if ind>=len(self.arr) or self.arr[ind]!=key:
            bisect.insort_left(self.arr,key)
        

    def remove(self, key: int) -> None:
        ind=bisect.bisect_left(self.arr,key)
        if ind<len(self.arr) and self.arr[ind]==key:
            self.arr.pop(ind)
        

    def contains(self, key: int) -> bool:
        ind=bisect.bisect_left(self.arr,key)
        
        if ind<len(self.arr) and self.arr[ind]==key:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)