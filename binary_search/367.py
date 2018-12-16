# 367. Valid Perfect Square
# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# a square number is 1+3+5+7+... Time Complexity O(sqrt(N)) 
# binary search. Time Complexity O(logN)
# Newton Method. See [this wiki page][1]. Time Complexity is close to constant, given a positive integer.

## 1,3,5,.. Sequence
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1: return True
        if num < 1: return False
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

## BS
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            if mid == num / mid:
                return True
            elif mid < num / mid:
                left = mid + 1
            else:
                right = mid - 1
        return False

## Newton
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1: return True
        candidate = self.helper(num, 1e-5)
        return candidate == num / candidate
        
    def helper(self, x, eps=1e-9):
        guess = x
        while abs(guess - x / guess) > eps:
            guess = (guess + x / guess) / 2
        return int(guess) 
### no need to calculate the exact sqrt
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1: return True
        
        guess = num
        while guess - num / guess > 0:
            guess = (guess + num / guess) // 2
            if guess == num / guess:
                return True
        return False