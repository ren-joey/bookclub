class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        return [True if c == max_val or c + extraCandies >= max_val else False for c in candies]