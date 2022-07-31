class Solution1:
    def minimumSum(self, num: int) -> int:
        nums = [int(n) for n in list(str(num))]
        nums.sort()
        sum1 = nums[0] * 10 + nums[2] + nums[1] * 10 + nums[3]
        sum2 = nums[0] * 100 + nums[1] * 10 + nums[2] + nums[3]
        return sum1 if sum1 <= sum2 else sum2

class Solution2:
    def minimumSum(self, num: int) -> int:
        d = sorted(str(num))
        return int(d[0] + d[2]) + int(d[1] + d[3])
