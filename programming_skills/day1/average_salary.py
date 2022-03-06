"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""


class Solution:
    def average(self, salary):
        maximum, length, total = 0, 0, 0
        minimum = salary[0]
        for sal in salary:
            if minimum > sal:
                minimum = sal
            if maximum < sal:
                maximum = sal
            total += sal
            length += 1
        return (total-minimum-maximum)/(length-2)


s = Solution()
print(s.average([4000, 3000, 1000, 2000]))
