class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for order, i in enumerate(nums):
            try:
                idx = nums.index(target - i)
                if (order == idx):
                    continue
                return [order, idx]
            except:
                continue

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx = 0
        while(len(nums) > 1):
            n = nums.pop(0)
            idx2 = nums.index(target - n) if target - n in nums else -1
            if (idx2 != -1):
                return [idx, idx + idx2 + 1]
            idx += 1

"""
Runtime: 75 ms, faster than 84.09% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 9.03% of Python3 online submissions for Two Sum.
"""
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i