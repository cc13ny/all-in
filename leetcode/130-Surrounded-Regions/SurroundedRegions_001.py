# Here's the AC code. However, there's two tricky points
# Please refer to http://www.cnblogs.com/grandyang/p/4555831.html


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            board = self.solveBFS(board, i, 0)
            board = self.solveBFS(board, i, len(board[i]) - 1)
        
        size = 0 if len(board) == 0 else len(board[0])
        for j in range(size):
            board = self.solveBFS(board, 0, j)
            board = self.solveBFS(board, len(board) - 1, j)
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O': 
                    tmp = list(board[i]) # 1st Tricky Point, it will be an error if board[i] = board[i][:j] + 'X' + board[i][j + 1:]
                    tmp[j] = 'X'
                    board[i] = ''.join(tmp)
                if board[i][j] == '$':
                    tmp = list(board[i])
                    tmp[j] = 'O'
                    board[i] = ''.join(tmp)
                    
    def solveBFS(self, board, i, j):
        if board[i][j] == 'O':
            tmp = list(board[i])
            tmp[j] = '$'
            board[i] = ''.join(tmp)
            if i > 0:
                self.solveBFS(board, i - 1, j)
            if j + 1 < len(board[i]):
                self.solveBFS(board, i, j + 1)
            if i + 1 < len(board):
                self.solveBFS(board, i + 1, j)
            if j > 1: # 2nd Tricky Point
                self.solveBFS(board, i, j - 1)
        return board
