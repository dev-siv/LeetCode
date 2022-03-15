class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for index, val in enumerate(nums):
            if val != 0:
                nums[count], nums[index] = val, nums[count]
                # if index != count:
                #     nums[index] = 0
                count += 1
        # return nums


if __name__ == "__main__":
    n = [10, 20, 0, 0, 30, 40]
    s = Solution()
    print(s.moveZeroes(n))


