'''
lc：33
搜做旋转排序数组;[4,5,6,7,0,1,2]
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        tmp = nums[n-1]
        while l < r:
            mid = (l + r ) // 2
            if nums[mid] <= tmp:
                r = mid
            else:
                l = mid + 1

        if target == tmp:
            return n-1
        if target > tmp:
            l,r = 0,l-1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            return l
        else:
            return -1




