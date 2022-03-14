class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n+1):
            div_3 = (i % 3 == 0)
            div_5 = (i % 5 == 0)
            if div_3 and div_5:
                answer.append("FizzBuzz")
            elif div_3 and not div_5:
                answer.append("Fizz")
            elif not div_3 and div_5:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(15))



