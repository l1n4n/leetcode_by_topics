# 51. N-Queens
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

# IDEA: put restrictions on dfs
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self._dfs(n, [],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in self.res]
        
    def _dfs(self, n, queens, left_diag, right_diag):
        row = len(queens)
        if row == n:
            self.res.append(queens)
            return
        for col in range(n):
            if col not in queens and row-col not in left_diag and row+col not in right_diag:
                self._dfs(n, queens+[col], left_diag+[row-col], right_diag+[row+col])