def finalValueAfterOperations(operations):
    return 2 * sum([1 for val in operations if val == "++X" or val == "X++"]) - len(operations)