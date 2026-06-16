class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin(left,right,ind):
            if left<=right:
                mid=left+(right-left)//2
                if matrix[ind][mid]==target:
                    return True
                elif matrix[ind][mid]<target:
                    return bin(mid+1,right,ind)
                else:
                    return bin(left,mid-1,ind)
            return False
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                if matrix[mid][0]<=target and target<=matrix[mid][-1]:
                    return bin(0,len(matrix[mid]),mid)
                elif matrix[mid][0]<target and target>matrix[mid][-1]:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return False
        return binary(0,len(matrix)-1)