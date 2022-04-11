def climbStairs(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    return climbStairs(n-1)+climbStairs(n-2)


if __name__ == "__main__":
    print(climbStairs(3))