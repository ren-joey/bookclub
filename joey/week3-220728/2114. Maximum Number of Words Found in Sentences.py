class Solution1:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for s in sentences:
            count = s.count(' ') + 1
            if (count > maximum):
                maximum = count
        return maximum

class Solution2:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([(s.count(' ') + 1) for s in sentences])
