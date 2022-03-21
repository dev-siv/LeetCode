def singleNumber(nums):
    nums.sort()
    for index in range(0, len(nums) - 1, 2):
        if nums[index] != nums[index + 1]:
            return nums[index]
    return nums[len(nums) - 1]


def singleNumber2(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    for k, v in d.items():
        if v == 1:
            return k


if __name__ == "__main__":
    print(singleNumber([4, 4, 1, 1, 2]))
