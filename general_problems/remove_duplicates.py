def removeDuplicates(nums):
    count = 1
    for index in range(len(nums)-1):
        if nums[index] != nums[index+1]:
            nums[count] = nums[index+1]
            count += 1
    return nums


if __name__ == "__main__":
    n = [1, 1, 2]
    print(removeDuplicates(n))