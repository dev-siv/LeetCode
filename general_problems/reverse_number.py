"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x):
        minimum_value = 2 ** (-32)
        maximum_value = 2 ** 32 + 1
        reverse_value = int(str(x)[::-1])
        if reverse_value < minimum_value or reverse_value > maximum_value:
            return 0
        else:
            return reverse_value


s = Solution()
print(s.reverse(1002))