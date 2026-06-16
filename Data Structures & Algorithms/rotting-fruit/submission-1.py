class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[]
        fresh=[]
        res=-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))
                if grid[i][j]==1:
                    fresh.append((i,j))
        if len(fresh)==0:
            return 0
        prev=[]
        while(rotten!=prev):
            prev=rotten[:]
            new=[]
            for i,j in rotten:
                if (i+1,j) in fresh:
                    new.append((i+1,j))
                    fresh.remove((i+1,j))
                if (i,j+1) in fresh:
                    new.append((i,j+1))
                    fresh.remove((i,j+1))
                if (i-1,j) in fresh:
                    new.append((i-1,j))
                    fresh.remove((i-1,j))
                if (i,j-1) in fresh:
                    new.append((i,j-1))
                    fresh.remove((i,j-1))
            
            if len(new)==0 and len(fresh)!=0:
                return -1
            rotten.extend(new)
            res+=1
        return res