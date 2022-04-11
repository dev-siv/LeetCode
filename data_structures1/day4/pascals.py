def generate(n):
    if n == 1:
        return [[1]]
    result = []
    for i in range(n):
        if i+1 < 3:
            result.append([1] * (i + 1))
        else:
            temp = [1] * (i+1)
            for j in range(1,len(temp)-1):
                # temp[j] =
                pass
    return result


if __name__ == "__main__":
    print(generate(5))
