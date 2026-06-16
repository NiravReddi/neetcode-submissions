class TimeMap:

    def __init__(self):
        self.dic=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic.keys():
            return ""
        else:
            r=-1
            for i in self.dic[key]:
                if i[0]<=timestamp:
                    r=i[1]
                else:
                    break
            if r==-1:
                return ""
            else:
                return r
        
