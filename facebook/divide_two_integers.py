def divide(dividend, divisor):
    if dividend == 0:
        return 0
    elif abs(divisor) == abs(dividend):
        if divisor < 0 or dividend < 0:
            return -1
        else:
            return 1
    elif divisor > dividend:
        return 0
    count = 1
    negative = 1
    if divisor < 0 and dividend < 0:
        negative = 1
        divisor *= -1
        dividend *= -1
    elif abs(divisor) != divisor or abs(dividend) != dividend:
        negative = -1
        divisor = abs(divisor)
        dividend = abs(dividend)
    temp = divisor
    while divisor < dividend:
        divisor = divisor + temp
        if divisor < dividend:
            count += 1
    return count * negative


if __name__ == "__main__":
    print(divide(-1, 1))
