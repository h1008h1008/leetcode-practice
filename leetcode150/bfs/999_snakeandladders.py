class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        mapping_board = [0]
        for row in range(n - 1, -1, -1):
            if (n-row) % 2 == 0:
                for col in range(n-1,-1,-1):
                    mapping_board.append(board[row][col])
            else:
                mapping_board += board[row]
        queue = deque()
        ans = 0
        queue.append((1,ans))
        visited = [False] * (n * n + 1)
        visited[1] = True
        while queue:
            (num, ans) = queue.popleft()
            if num == n * n:
                return ans
            for k in range(1, 7):
                if num + k > n * n:
                    continue
                dest = mapping_board[num + k] if mapping_board[num + k] != -1 else num + k
                if not visited[dest]:
                    visited[dest] = True
                    queue.append((dest, ans+1))
        return -1
                

        