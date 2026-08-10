class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left, right = 0, len(heights) - 1
        while left < right:
            smaller_side = heights[left] if heights[left] < heights[right] else heights[right]
            area = max(area, smaller_side * (right - left))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return area