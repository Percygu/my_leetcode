#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 1,len(nums)-1               #定义边界，n个抽屉,因为有n+1个数，这个重复的数一定会出现在前面的[1,n]区间内
        while l<r:
            mid = (l+r)//2
            cnt = 0             #抽屉原理，因为数组里的数都是小于n+1的，n个抽屉，n+1个数，必然有1个抽屉放了两个数
            for num in nums:
                if num <= mid and num>=l:
                    cnt +=1     #求整个数组中比mid大的数的个数
            if cnt>mid-l+1:
                r = mid
            else:
                l = mid +1
        return r
      
# @lc code=end

