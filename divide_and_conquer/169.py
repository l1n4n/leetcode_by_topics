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

# A better d&c solution https://leetcode.com/problems/majority-element/discuss/177183/C++-Divide-and-conquer-O(N)-solution-(4-ms-beats-100)
# similar with Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: return nums[0]
        # when n is odd, the last number will not be paired up
        if n % 2:
            if nums.count(nums[-1]) > n//2:
                return nums[-1]
        # pair up and keep the candidates --> cut (at least) size in half
        temp = []
        for i in range(0, n//2):
            if nums[2*i] == nums[2*i+1]:
                temp.append(nums[2*i])
        return self.majorityElement(temp)
            
