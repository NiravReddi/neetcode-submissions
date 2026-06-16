class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix=[]
        for i in range(len(matrix)):
            rowsum=0
            thisrow=[]
            for j in range(len(matrix[0])):
                if len(self.prefix)==0:
                    rowsum+=matrix[i][j]
                    thisrow.append(rowsum)
                else:
                    rowsum+=matrix[i][j]
                    thisrow.append(self.prefix[-1][j]+rowsum)
            self.prefix.append(thisrow)
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=self.prefix[row2][col2]
        if row1-1<0 and col1-1<0:
            return res
        elif row1-1<0 and col1-1>=0:
            return res-self.prefix[row2][col1-1]
        elif row1-1>=0 and col1-1<0:
            return res-self.prefix[row1-1][col2]
        else:
            return res-self.prefix[row1-1][col2]-(self.prefix[row2][col1-1]-self.prefix[row1-1][col1-1])
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)