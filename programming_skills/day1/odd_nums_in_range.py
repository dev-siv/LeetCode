"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""


class Solution:
    def countOdds(self, low, high):
        # if low + 1 == high:
        #     return 1
        if low % 2 == 0 and high % 2 == 0:
            return (high-low-1)//2 + 1
        elif low % 2 != 0 and high % 2 != 0:
            return ((high+1-low)//2) + 1

        return (high+1-low) // 2


s = Solution()
print(s.countOdds(8, 10))
print(s.countOdds(3, 7))
print(s.countOdds(4, 9))
print(s.countOdds(3,4))