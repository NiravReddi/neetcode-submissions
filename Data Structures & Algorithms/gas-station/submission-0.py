class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dic=defaultdict(bool)
        def dfs(i,dest,c):
            if i==dest:
                return True
            if (i,c) in dic.keys():
                return dic[(i,c)]
            if (c-cost[i]+gas[i])>=0:
                dic[(i,c)]= dfs((i+1)%len(gas),dest,c-cost[i]+gas[i])
                return  dic[(i,c)]
            else:
                dic[(i,c)]=False
                return dic[(i,c)]
        for i in range(len(gas)):
            if gas[i]>=cost[i] and dfs((i+1)%len(gas),i,gas[i]-cost[i]) :
                return i
            
        return -1