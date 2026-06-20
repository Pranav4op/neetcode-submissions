class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            a = set()
            for j in i:
                if j == ".":
                    continue
                if j in a:
                    return False
                a.add(j)
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for i in range(9):
            a = set()
            for j in range(3):
                for k in range(3):
                    row = (i//3)*3+j
                    col = (i%3)*3+k
                    if board[row][col]==".":
                        continue
                    if board[row][col] in a:
                        return False
                    a.add(board[row][col])

        return True
            
            