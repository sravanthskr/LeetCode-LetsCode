class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        found=False
        for i in range(len(matrix)-1):
    
            for j in range(len(matrix[0])-1):
                if matrix[i][j]==matrix[i+1][j+1]:
                    found=True
                else:
                    found=False
                    break
        return found