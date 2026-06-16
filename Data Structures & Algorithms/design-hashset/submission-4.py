class MyHashSet:

    def __init__(self):
        self.dic={}
        

    def add(self, key: int) -> None:
        if key in self.dic.keys():
            self.dic[key].append(key)
        else:
            self.dic[key]=[key]

        

    def remove(self, key: int) -> None:
        if key in self.dic.keys() and len(self.dic[key])>=1:
            del self.dic[key]
        

    def contains(self, key: int) -> bool:
        print(self.dic)
        return key in self.dic.keys()
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)