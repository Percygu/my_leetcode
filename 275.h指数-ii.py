#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, nums: List[int]) -> int:
        n = len(nums)         #找一个数h，使得数组中至少有h个数大于等于h
        l,r = 0,n             #确定二分边界，0满足，h<=n
        while l<r:
            mid = (1+l+r)//2   #h满足，则h-1一定满足，向下取整
            if mid <= nums[len(nums)-mid]:  #要让h个数大于等于h,则边界点的后一个数一定大于等于h，这个性质满足左边区间
                l = mid
            else:
                r = mid -1
        return r
        
# @lc code=end

