def plusOne(digits):
    base = 1
    digit = 0
    for val in digits[::-1]:
        digit += val * base
        base *= 10
    digit += 1
    result = []
    while digit != 0:
        remainder = digit % 10
        result.insert(0, remainder)
        digit = digit // 10
    return result


if __name__ == "__main__":
    print(plusOne([1, 2, 3]))
