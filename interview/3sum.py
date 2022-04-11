class Solution:
    def threeSum(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        print(i, j, k)
                        result.append([nums[i], nums[j], nums[k]])

        return result


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(arr))
