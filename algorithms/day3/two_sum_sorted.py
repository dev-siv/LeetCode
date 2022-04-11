"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""


class Solution:
    def twoSum(self, numbers, target) :
        for index, value in enumerate(numbers):
            if target-value in numbers:
                return [index, numbers.index(target-value)]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
