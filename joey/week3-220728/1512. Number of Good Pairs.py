class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        leng = len(nums)
        goodPairs = 0
        head = 0
        tail = 1
        while(head < leng - 1):
            if (nums[head] == nums[tail]):
                goodPairs += 1
            if (tail == leng - 1):
                head += 1
                tail = head + 1
            else:
                tail += 1
        return goodPairs

class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(c * (c - 1) // 2 for c in Counter(nums).values())