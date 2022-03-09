class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[count] = nums[index]
                if count != index:
                    nums[index] = 0
                count += 1



if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([1, 2, 0, 3, 4, 0, 0, 6])
