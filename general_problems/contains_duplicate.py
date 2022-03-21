def containsDuplicate(nums):
    seen = {}
    for n in nums:
        if n in seen:
            return True
        seen[n] = True
        # if seen[n] == 2:
        #     return False
    return False


if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))