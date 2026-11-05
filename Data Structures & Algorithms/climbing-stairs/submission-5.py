class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2

        for _ in range(n - 1):
            c = b + a
            a = b
            b = c

        return a