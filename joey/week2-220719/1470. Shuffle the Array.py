class Solution1:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [None] * (2 * n)

        for i in range(0, n):
            arr[2 * i] = nums[i]

        for j in range(n, 2 * n):
            print(nums[j])
            arr[(j - n + 1) * 2 - 1] = nums[j]

        return arr

"""
Runtime: 68 ms, faster than 84.31% of Python3 online submissions for Shuffle the Array.
Memory Usage: 13.9 MB, less than 99.41% of Python3 online submissions for Shuffle the Array.
"""
class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [None] * (2 * n)

        for idx, num in enumerate(nums[:n]):
            arr[2 * idx] = num

        for idx, num in enumerate(nums[n:]):
            arr[(idx - n + 1) * 2 - 1] = num

        return arr