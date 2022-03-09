class Solution:
    def sortedSquares(self, nums):
        res = []
        for index, val in enumerate(nums):
            res.insert(index, val*val)

        print(res)


s = Solution()
s.sortedSquares([-3, 0, 1, 2])