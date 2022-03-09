from collections import deque


class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q = deque(nums)
        q.rotate(k)
        for index, value in enumerate(q):
            nums[index] = value



s = Solution()
n = [1, 2, 3, 4, 5, 6, 7]
k = 3
s.rotate(n, k)
