def merge_sort(nums,l,r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(nums,l,mid)
    merge_sort(nums,mid+1,r)

    # 合并两个有序数组
    i,j = l,mid+1
    q = []
    while i <= mid and j <= r:
        if nums[i] < nums[j]:
            q.append(nums[i])
            i += 1
        else:
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

if __name__ == "__main__":
    nums = [3,6,9,5,8,4,2,1,7,0]
    merge_sort(nums,0,len(nums)-1)
    print(nums)




