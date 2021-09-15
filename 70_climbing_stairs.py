def climb_stairs2(n: int) -> int:
    if n == 1 or n == 2:
        return n
    n1 = 1
    n2 = 2
    t = 0

    for i in range(3, n + 1):
        t = n1 + n2
        n1 = n2
        n2 = t

    return t


class StairClimber:
    # total variable needed for the recursive solution
    total = 0

    # recursive, mathy way that's slow for sufficiently big numbers
    def climb_stairs(self, n: int) -> int:
        if n == 0:
            self.total += 1

        if n >= 1:
            self.climb_stairs(n - 1)

        if n >= 2:
            self.climb_stairs(n - 2)

        return self.total

    # standard, boring dynamic programming way


print(climb_stairs2(3))
print(climb_stairs2(38))

