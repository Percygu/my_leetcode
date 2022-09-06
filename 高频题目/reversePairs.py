class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)


    def mergeSort(self,nums,l,r):
        res = 0
        if l > r:
            return
        mid = (l + r) // 2
        res += self.mergeSort(nums,l,mid)
        res += self.mergeSort(nums,mid+1,r)

        # 合并两个有序链表
        q = []
        i,j = l,mid+1
        while i <=mid and j <= r:
            if nums[i] <= nums[j]:
                q.append(nums[i])
                i += 1
            else:
                res += (j-i+1)
                q.append(nums[j])
                j += 1
        while i <= mid:
            q.append(nums[i])
            i += 1
        while j <= r:
            q.append(nums[j])
            j += 1

        i,j = l,0
        while j < len(q):
            nums[i] = q[j]
            i += 1
            j += 1
        return res