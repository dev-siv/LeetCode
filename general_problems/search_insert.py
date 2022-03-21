def searchInsert(nums, target):
    # len(nums)
    if nums[0] > target:
        return 0
    elif nums[len(nums) - 1] < target:
        return len(nums)
    left = 0
    right = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target < nums[mid + 1]:
            return mid + 1
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1


if __name__ == "__main__":
    print(searchInsert([1, 3, 5, 6], 7))
