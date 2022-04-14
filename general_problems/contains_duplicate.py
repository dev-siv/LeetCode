def containsDuplicate(nums):
    seen = {}
    for n in nums:
        if n in seen:
            return True
        seen[n] = True
    return False


def contains_duplicate(nums):
    track = set()
    left, right = 0, len(nums) - 1
    if len(nums) == 1:
        return False
    while left <= right:
        if nums[left] in track:
            return True
        track.add(nums[left])
        if nums[right] in track:
            return True
        track.add(nums[right])
        left += 1
        right -= 1
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 5, -2, -4, 0]))
