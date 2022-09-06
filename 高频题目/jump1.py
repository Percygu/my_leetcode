class Solution:
    def jump(self, nums: List[int]) -> int:
       n = len(nums)
       steps,end = 0,0
       maxPos = 0
       for i in range(n-1):
           maxPos = max(maxPos,i + nums[i])
           if end == maxPos:
               steps += 1
               end = maxPos
       return steps
