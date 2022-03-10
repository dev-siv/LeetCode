def subtractProductAndSum_f(n):
    sum_of_digits = 0
    product_of_digits = 1
    while n != 0:
        remainder = n % 10
        sum_of_digits += remainder
        product_of_digits *= remainder
        n = n // 10
    return product_of_digits - sum_of_digits


if __name__ == "__main__":
    num = 12345
    print(subtractProductAndSum_f(num))
