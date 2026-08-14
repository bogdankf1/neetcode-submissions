class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                saved_i, saved_h = stack.pop()
                max_area = max(max_area, saved_h * (i - saved_i))
                start = saved_i
            stack.append((start, h))

        for saved_i, saved_h in stack:
            max_area = max(max_area, saved_h * (len(heights) - saved_i))
        return max_area 