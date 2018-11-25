# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# DIVIDE into halves, leave the mid one as the center of the subarray
# CAVEAT:
## for the left part, start adding from the tail, cuz the subarray has to be around the mid
## use a variable to keep the lower bound i.e. max (init as 0), use a seperate variable to keep the current sum
## process data at this level: left max + mid + right max
## for the right part, range(mid+1, right+1) to get nums[right] 
# TRICKS:
## when the left idx < right idx, return the smallest integer so that it would not affect the result

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dnc_max_subarr(nums, 0, len(nums)-1)
    
    def dnc_max_subarr(self, nums, l, r):
        # if problem is none, return
        if l > r: return -2147483647
        if l == r: return nums[l]
        # prepare data
        mid = l + (r-l)//2
        # conquer subproblems
        left_ans = self.dnc_max_subarr(nums, l, mid-1)
        right_ans = self.dnc_max_subarr(nums, mid+1, r)
        # process data at current level
        left_max, left_sum, right_max, right_sum = 0, 0, 0, 0
        for i in range(mid-1, l-1, -1):
            left_sum += nums[i]
            left_max = max(left_max, left_sum)
        for i in range(mid+1, r+1):
            right_sum += nums[i]
            right_max = max(right_max, right_sum) 
        # generate the final result
        return max(left_max + nums[mid] + right_max, left_ans, right_ans)