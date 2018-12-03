# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

#  https://leetcode.com/problems/generate-parentheses/discuss/196791/Java-and-Python-DFS-backtrack-using-recursion.
# BACKTRACK & RECURSION & DIVIDE AND CONQURE all need a helper function
# The first line of the helper function is the stop condition
## Google java style guide

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self._gen(ans, n, n, "")
        return ans
    
    def _gen(self, lis, left, right, comb):
        if left == right == 0:
            lis.append(comb)
            
        if left > 0:
            self._gen(lis, left-1, right, comb+'(')
        
        if right > left:
            self._gen(lis, left, right-1, comb+')')
