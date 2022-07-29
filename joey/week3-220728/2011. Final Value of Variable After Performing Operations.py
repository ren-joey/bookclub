"""
Runtime: 49 ms, faster than 97.09% of Python3 online submissions for Final Value of Variable After Performing Operations.
Memory Usage: 13.8 MB, less than 54.80% of Python3 online submissions for Final Value of Variable After Performing Operations.
"""
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for operation in operations:
            res += 1 if '+' in operation else -1
        return res