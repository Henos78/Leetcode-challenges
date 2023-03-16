class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dic = {0: 1}
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in dic:
                count += dic[curr_sum - k]
            if curr_sum in dic:
                dic[curr_sum] += 1
            else:
                dic[curr_sum] = 1


        return count
