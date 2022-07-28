class Solution1:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])
        return ans

class Solution2:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]
