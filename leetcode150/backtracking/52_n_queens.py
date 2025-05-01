class Solution(object):
    def totalNQueens(self, n):
        ans = [0]
        board = [[0 for _ in range(n)] for _ in range(n)]
        
        def place_queen(i, j):
            board[i][j] = 2
            for k in range(1, n):
                for dx, dy in [(0,1), (1,0), (1,1), (1,-1)]:
                    if 0 <= i+dx*k < n and 0 <= j+dy*k < n:
                        board[i+dx*k][j+dy*k] += 1
                    if 0 <= i-dx*k < n and 0 <= j-dy*k < n:
                        board[i-dx*k][j-dy*k] += 1
        
        def get_queen(i, j):
            board[i][j] = 0
            for k in range(1, n):
                for dx, dy in [(0,1), (1,0), (1,1), (1,-1)]:
                    if 0 <= i+dx*k < n and 0 <= j+dy*k < n:
                        board[i+dx*k][j+dy*k] -= 1
                    if 0 <= i-dx*k < n and 0 <= j-dy*k < n:
                        board[i-dx*k][j-dy*k] -= 1
        
        def backtrack(row):
            if row == n:
                ans[0] += 1
                return
            for col in range(n):
                if board[row][col] == 0:
                    place_queen(row, col)
                    backtrack(row + 1)
                    get_queen(row, col)
        
        backtrack(0)
        return ans[0]


class Solution(object):
    def totalNQueens(self, n):
        ans = [0]
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            if row == n:
                ans[0] += 1
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return ans[0]
