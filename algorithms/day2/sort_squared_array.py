class Solution:
    def sortedSquares(self, nums):
        res = [None] * len(nums)
        left, right = 0, len(nums) - 1
        for index in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[index] = nums[left] ** 2
                left += 1
            else:
                res[index] = nums[right] ** 2
                right -= 1
        return res


s = Solution()
print(s.sortedSquares([-3, 0, 1, 2]))
