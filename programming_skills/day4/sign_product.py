class Solution:
    def arraySign(self, nums):
        negative_count = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                negative_count += 1
        if negative_count % 2 != 0:
            return -1
        return 1


if __name__ == "__main__":
    s = Solution()
    arr = [-1, -2, -3, -4, 3, 2, 1]
    print(s.arraySign(arr))
    arr = [1, 5, 0, 2, -3]
    print(s.arraySign(arr))
    arr = [-1, 1, -1, 1, -1]
    print(s.arraySign(arr))
