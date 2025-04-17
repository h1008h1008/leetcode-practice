class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0,n):
            for j in range(i + 1,n):
                if i != j:
                    matrix[i][j],matrix[j][i]  = matrix[j][i],matrix[i][j]
        for i in range(0,n):
            for j in range(0,n/2):
                matrix[i][j],matrix[i][n-1-j]  = matrix[i][n-1-j],matrix[i][j]
        # when doing transpose only do half of the matrix
        