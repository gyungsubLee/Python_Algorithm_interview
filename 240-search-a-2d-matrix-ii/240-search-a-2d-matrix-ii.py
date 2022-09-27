class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        row, col = len(matrix[0])-1, 0
        while row >= 0 and col < len(matrix):
            if matrix[col][row] < target:
                col += 1
            elif matrix[col][row] > target:
                row -= 1
            else:
                return True
        return False

                
        
        
            