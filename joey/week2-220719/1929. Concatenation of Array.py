class Solution1:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums.append(nums[i])
        return nums
    
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums