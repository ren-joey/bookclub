class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candiesCheckList = []

        for i in candies:
            candiesCheckList.append(i + extraCandies >= max(candies))

        return candiesCheckList