"""
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


s = Solution()
print(s.containsDuplicate([1, 2, 3, 4]))