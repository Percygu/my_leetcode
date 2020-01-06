#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r =0, len(nums)-1
        while l<r:
            mid = (l+r)//2   #峰值满足nums[mid]>nums[mid+1]
            if nums[mid]>nums[mid+1]: #mid在右边区间，且端点包含在右边区间，可取等号
                r = mid 
            else:l =mid+1
        return l
        
# @lc code=end

