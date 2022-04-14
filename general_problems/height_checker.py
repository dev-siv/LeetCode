def heightChecker(heights):
    count = 0
    for i in range(len(heights)):
        for j in range(len(heights)):
            if heights[i] > heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                count += 1

    return count


if __name__ == "__main__":
    print(heightChecker([1, 1, 4, 2, 1, 3]))