class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        pre_sum = [0] * 51

        for start, end in ranges:
            for i in range(start, end + 1):
                pre_sum[i] += 1

        for i in range(left, right + 1):
            if pre_sum[i] == 0:
                return False

        return True
