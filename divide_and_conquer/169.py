# 169. Majority Element
# Given an array of size n, find the majority element. The majority element is the element that appears more than  n/2  times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# DIVIDE AND CONQUER [NOT THE BEST WAY TO SOLVE IT]
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = left + (right-left)//2
        lm, rm = self.helper(nums, left, mid), self.helper(nums, mid+1, right)
        if lm == rm: return lm
        # mid+1, right+1 !!!!!
        return lm if nums[left: mid+1].count(lm) > nums[mid+1: right+1].count(rm) else rm