class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                cnt = 0
                dx = [-1, 0, 1]
                dy = [-1, 0, 1]
                for di in dx:
                    for dj in dy:
                        if di == 0 and dj == 0:
                            continue
                        idi, jdj = i + di, j + dj
                        if 0 <= idi < m and 0 <= jdj < n and board[idi][jdj] & 1 > 0:
                            cnt += 1
                if board[i][j]:
                    if 2 <= cnt <= 3:
                        board[i][j] = 3
                elif cnt == 3:
                    board[i][j] = 2

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = board[i][j] >> 1
