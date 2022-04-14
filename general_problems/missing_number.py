def missingNumber(nums):
    for n in range(len(nums) + 1):
        try:
            nums.remove(n)
        except ValueError:
            return n


def missing_number(nums):
    n = len(nums)
    return ((n * (n + 1)) // 2) - sum(nums)


if __name__ == "__main__":
    print(missingNumber([3, 0, 1]))
    print(missing_number([3, 0, 1]))
