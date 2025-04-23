class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(0,len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][len(triangle[i-1])-1]
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[len(triangle)-1])
            
        #def minimumTotal(triangle):
    # # Start from the second-to-last row and move upward
    # for row in range(len(triangle) - 2, -1, -1):
    #     for col in range(len(triangle[row])):
    #         # Update the current cell to the minimum sum of the two possible paths below
    #         triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # # The top element now contains the minimum path sum
    # return triangle[0][0]
# try bottom-up next time