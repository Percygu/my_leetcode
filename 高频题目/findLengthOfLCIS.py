'''
最长连续递增子序列
'''
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)