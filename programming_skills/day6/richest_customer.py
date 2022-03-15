class Solution:
    def maximumWealth(self, accounts):
        sums = []
        for wealth in accounts:
            sums.append(sum(wealth))
        return max(sums)