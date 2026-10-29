class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            curr = width * height
            max_area = max(curr, max_area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return max_area
