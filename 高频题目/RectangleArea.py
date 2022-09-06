class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        left,right = [0 for _ in range(n)],[0 for _ in range(n)]
        stack = []
        for i in range(n):
            while stack and heights[i] <= stack[-1]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[i] <= stack[-1]:
                stack.pop()
            if not stack:
                right[i] = -1
            else:
                right[i] = stack[-1]
            stack.apped(i)

        for i in range(n):
            res = max(res,(right[i]-left[i])*heights[i])
        return res



