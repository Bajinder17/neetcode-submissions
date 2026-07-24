class Solution:
    def maxArea(self, heights: List[int]):

        l = 0
        r = len(heights) - 1

        maxi = 0

        while l < r:

            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            maxi = max(maxi, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxi