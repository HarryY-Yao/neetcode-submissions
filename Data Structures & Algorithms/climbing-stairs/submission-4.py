class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2

        for i in range(1, n):
            c = a + b
            a = b
            b = c

        return a