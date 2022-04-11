"""
https://leetcode.com/problems/remove-element/
"""


#
def removeElement(nums, val):
    count = 0
    for index, v in enumerate(nums):
        if val == v and index+1 < len(nums):
            nums[index] = nums[index+1]
            # nums[index+1] = 0
            count += 1
    return len(nums) - count


if __name__ == "__main__":
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
