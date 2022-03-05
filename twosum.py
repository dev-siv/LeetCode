"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


def twoSum(nums, target):
    secondary_list = []
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in secondary_list:
            return [secondary_list.index(remainder), i]
        else:
            secondary_list.append(nums[i])


if __name__ == "__main__":
    print(twoSum([2, 7, 5, 11], 9))
