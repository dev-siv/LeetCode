"""https://leetcode.com/problems/search-insert-position/"""


class Solution:
    def searchInsert(self, nums, target):
        left, mid = 0, 0
        right = len(nums) - 1
        if target < nums[left]:
            return left
        elif target > nums[right]:
            return right + 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid

        if target <= nums[left]:
            return left
        elif target == nums[right]:
            return right


s = Solution()
nums = [1, 3, 5, 6]
target = 2

print(s.searchInsert(nums, target))



