"""https://leetcode.com/problems/two-sum/"""


def twoSum(nums, target):
    second_list = []
    for index, val in enumerate(nums):
        remainder = target - val
        if remainder in second_list:
            return [second_list.index(remainder), index]
        else:
            second_list.append(val)


if __name__ == "__main__":
    n = [2, 7, 11, 15]
    t = 18
    print(twoSum(n, t))
