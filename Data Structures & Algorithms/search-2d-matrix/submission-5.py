class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_col(ind,left,right):
            if left<=right and right<len(matrix[0]):
                mid=left+((right-left)//2)
                if matrix[ind][mid]==target:
                    return True
                elif matrix[ind][mid]<target:
                    return binary_col(ind,mid+1,right)
                else:
                    return binary_col(ind,left,mid-1)
            return False
        def binary_row(left,right):
            if left<=right:
                mid=left+((right-left)//2)
                if matrix[mid][0]<=target<=matrix[mid][-1]:
                    return binary_col(mid,0,len(matrix[0])-1)
                elif matrix[mid][-1]<target:
                    return binary_row(mid+1,right)
                else:
                    return binary_row(left,mid-1)
            return False
        return binary_row(0,len(matrix)-1)