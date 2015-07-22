class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            tmp = set()
            for t in board[i]:
                if t != '.':
                    if t in tmp:
                        return False
                    else:
                        tmp.add(t)
                    
        for j in range(9):
            tmp = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in tmp:
                        return False
                    else:
                        tmp.add(board[i][j])
        for m in range(3):
            for n in range(3):
                tmp = set()
                for i in range(0 + 3*m, 3 + 3*m):
                    for j in range(0 + 3*n, 3 + 3*n):
                        if board[i][j] != '.':
                            if board[i][j] in tmp:
                                return False
                            else:
                                tmp.add(board[i][j])
        
        return True
