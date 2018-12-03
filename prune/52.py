# 52. N-Queens II
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        self._dfs(n, [], [], [])
        return self.ans
    
    def _dfs(self, n, queens, left_d, right_d):
        row = len(queens)
        if row == n:
            self.ans += 1
            return
        for col in range(n):
            if col not in queens and row-col not in left_d and row+col not in right_d:
                self._dfs(n, queens+[col], left_d+[row-col], right_d+[row+col])
        
