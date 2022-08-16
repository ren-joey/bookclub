class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)

        oddMax = length if length % 2 == 0 else length + 1

        res = 0

        for subLength in range(1, oddMax, 2):
            for index in range(length - subLength + 1):
                tmp = arr[index: index + subLength]
                res += sum(tmp)

        return res