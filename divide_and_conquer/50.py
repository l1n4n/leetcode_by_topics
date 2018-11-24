# 50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n.
# IDEA: DIVIDE AND CONQUER

# iterative
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
# recursive
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n < 0: return 1/self.myPow(x, -n)
        if n & 1: return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)