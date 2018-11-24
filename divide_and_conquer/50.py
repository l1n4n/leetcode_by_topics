# 50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n.
# IDEA: DIVIDE AND CONQUER
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n < 0: 
            n, x = -n, 1/x
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res