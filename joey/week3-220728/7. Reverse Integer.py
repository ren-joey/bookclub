class Solution1:
    def reverse(self, x: int) -> int:
        print(pow(2, 32))
        sign = '-' if x < 0 else ''
        res = int(sign + str(x)[::-1].replace('-', ''))
        if (res > pow(2, 31) - 1 or res < -(pow(2, 31))):
            res = 0
        return res

class Solution2:
    def reverse(self, x):
        s = -1 if x < 0 else 1
        r = int(str(s*x)[::-1])
        return s*r * (r < 2**31)
