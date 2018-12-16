# 69. Sqrt(x)
# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# BS
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: return x
        left, right, mid = 1, x, 0
        while left <= right:
            mid = left + (right - left) // 2
            #if mid * mid == x:
            if mid == x / mid: # to avoid overflow
                return mid
            elif mid < x / mid:
                left = mid + 1
                # res = mid # keep the lower int bound in case x's sqrt is not an integer
            else:
                right = mid - 1
        return left - 1
# Newton
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: return x
        guess = x
        while guess > x / guess:
            guess = (guess + x / guess) // 2
        return int(guess)        