def romanToInt(num):
    result = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    previous = 0
    for val in num[::-1]:
        if roman[val] >= previous:
            result += roman[val]
        else:
            result -= roman[val]
        previous = roman[val]
    return result


if __name__ == "__main__":
    print(romanToInt("MCMXCIV"))