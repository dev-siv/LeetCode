def majorityElement(nums):
    for n in set(nums):
        if nums.count(n) > len(nums) / 2:
            return n


def majorityElement(nums):
    left, right = 0, len(nums) - 1
    track = {}
    while left <= right:
        track[nums[left]] = track.get(nums[left], 0) + 1
        if track[nums[left]] > len(nums) / 2:
            return nums[left]
        track[nums[right]] = track.get(nums[right], 0) + 1
        if track[nums[right]] > len(nums) / 2:
            return nums[right]
        left += 1
        right -= 1


if __name__ == "__main__":
    print(majorityElement([3, 3, 4]))
