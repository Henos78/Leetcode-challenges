class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expect= sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if expect[i]!= heights[i]:
                count+=1
        return count
        