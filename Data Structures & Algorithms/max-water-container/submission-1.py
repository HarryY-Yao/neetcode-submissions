class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maximum = 0
        while (r > l):
            width = r - l
            height = min(heights[r], heights[l])

            maximum = max(maximum, height * width)

            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1
        
        return maximum
