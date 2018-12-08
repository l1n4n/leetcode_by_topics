# 36
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                if (i, c) in seen or (c, j) in seen or (i//3, j//3, c) in seen:
                    return False
                seen.add((i, c))
                seen.add((c, j))
                seen.add((i//3, j//3, c))
        return True