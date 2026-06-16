class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic=defaultdict(int)
        ind=0
        for i in s:
            dic[i]=ind
            ind+=1
        res=[]
        def check(st,ind):
            for i in st:
                if dic[i]>ind:
                    return False
            return True
        st=set()
        lastind=-1
        for ind in range(len(s)):
            st.add(s[ind])
            if check(st,ind):
                st=set()
                res.append(ind-lastind)
                lastind=ind
        return res
