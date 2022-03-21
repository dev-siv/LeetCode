"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""


class Solution:
    def average(self, salary):
        maximum, total, minimum = 0, 0, salary[0]
        for sal in salary:
            if minimum > sal:
                minimum = sal
            if maximum < sal:
                maximum = sal
            total += sal
        return (total - (minimum + maximum)) / (len(salary) - 2)


s = Solution()
print(s.average([4000, 3000, 1000, 2000]))
