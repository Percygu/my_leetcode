class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            last = 0
            while stack and height[stack[-1]] <= height[i]:
                t = stack.pop()
                res += (i-t-1) * (height[t] - last)
                last = height[t]
            if stack:
                res += (i-stack[-1]-1) * (height[i]-last)
            stack.append(i)
        return res