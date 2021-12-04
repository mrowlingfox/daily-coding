class Solution:
    def is_multiple_of(self, n, div):
        return n % div == 0

    def parse_number(self, x):
        if self.is_multiple_of(x, 15):
            return "FizzBuzz"
        if self.is_multiple_of(x, 5):
            return "Buzz"
        if self.is_multiple_of(x, 3):
            return "Fizz"
        return str(x)

    def solve(self, n):
        return [self.parse_number(x) for x in range(1, n+1)]
