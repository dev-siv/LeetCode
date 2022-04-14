def missingNumber(nums):
    for n in range(len(nums)+1):
        try:
            nums.remove(n)
        except ValueError:
            return n
    # return nums


if __name__ == "__main__":
    print(missingNumber([3,0,1]))
