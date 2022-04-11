"""
https://leetcode.com/problems/remove-element/
"""


#
def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[count] = 0, nums[i]
            count += 1
    return nums, count


if __name__ == "__main__":
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
