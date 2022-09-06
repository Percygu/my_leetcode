class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        n = len(height)
        stk = []
        for i in range(n):      #单调栈，每一个元素在入栈之前保证栈顶元素是它左边的第一个比它打的元素，不满足，则要进行栈的弹出操作，以满足要求
            last = 0
            while stk and height[stk[-1]] <= height[i]:
                t = stk[-1]  # 存下栈顶元素的值
                del stk[-1]     #删除栈顶元素
                res += (i-t-1) * (height[t] - last)  # 因为只有当当前矩形块高度大于前一个矩形块高度时才可能收集雨水，此时height[t]是前一个矩形块的高度,相邻元素res+=0,这种情况说明左边高度小于右边高度
                last = height[t]
            if stk:
                res += (i-stk[-1]-1) * (height[i]-last)  # 这种情况说明左边高度大于右边高度
            stk.append(i)
        return res      