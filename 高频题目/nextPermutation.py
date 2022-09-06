'''
lc:31
下一个排列
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        k = i
        # 此时i为拐点
        if i > 0:
            j = i -1
            # 寻找怪嗲你右侧第一个比tmp大的数做交换
            i = n-1
            while i >= k and nums[i] <= nums[j]:
                i -= 1
            if i >= k:
                nums[j],nums[i] = nums[i],nums[j]

        i,j = k,n-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        return nums






