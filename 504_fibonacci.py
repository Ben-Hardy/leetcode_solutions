# this is the math way of doing this. There's iterative ways that are faster but more space-intensive
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

s = Solution()

print(s.fib(0))
print(s.fib(1))
print(s.fib(2))
print(s.fib(10))
# print(s.fib(50)) # this will take a while
