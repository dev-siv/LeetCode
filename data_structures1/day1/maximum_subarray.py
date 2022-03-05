"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.
A subarray is a contiguous part of an array.
"""


class Solution:
    def maxSubArray(self, nums):
        maximum = float("-inf")
        max_value = 0
        for i in range(len(nums)):
            max_value += nums[i]
            if maximum < max_value:
                maximum = max_value

            if max_value < 0:
                max_value = 0

        return maximum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
