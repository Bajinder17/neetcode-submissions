class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxi = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                idx = i - j
                mini = min(heights[i], heights[j])
                vol = idx * mini
                maxi = max(vol, maxi)
        
        return maxi