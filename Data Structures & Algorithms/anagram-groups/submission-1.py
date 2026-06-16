class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        res=[]
        def make_store(s):
            st=[0]*26
            for i in s:
                st[97-ord(i)]+=1
            dic[tuple(st)].append(s)
        for i in strs:
            make_store(i)
        for i in dic.keys():
            res.append(dic[i])
        return res