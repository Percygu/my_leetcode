def merge_sort(arr,l,r): 
    if l >= r:                  # 区间只有一个元素了
        return
    mid = (l + r) // 2
    merge_sort(arr,l,mid)       # 区间中不止一个元素，递归执行归并排序
    merge_sort(arr,mid+1,r)     

    #  此时以mid为重点，左右区间都是有序区间，合并两个区间即可
    i,j = l,mid+1
    q = []
    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            q.append(arr[i])
            i += 1
        else:
            q.append(arr[j])
            j += 1
    while i <= mid:
            q.append(arr[i])
            i += 1
    while j <= r:
            q.append(arr[j])
            j += 1

    # 把q里的元素复制到数组arr里去
    i,j = l,0
    while j < len(q):
        arr[i] = q[j]
        i += 1
        j += 1
    
    return arr

#    利用归并排序求逆序对
def merge_sort1(arr,l,r):        # 函数返回逆序对个数
    if l >= r:                  # 区间只有一个元素了
        return 0
    res = 0
    mid = (l + r) // 2
    res += merge_sort1(arr,l,mid)       # 左边区间逆序对个数
    res += merge_sort1(arr,mid+1,r)     # 右边区间逆序对个数

    #  此时以mid为重点，左右区间都是有序区间，合并两个区间即可
    i,j = l,mid+1
    q = []
    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            q.append(arr[i])
            i += 1
        else:                          # 说明arr[j] 比 arr[i] 小，两个个区间之间存在逆序对，又因为区间是排好序的，则第一个区间i后面的元素都比arr[j]大，都可以构成逆序对
            res += mid - i + 1         #  所以两个区间之间的逆序对的个数就是左边区间i到mid的元素个数
            q.append(arr[j])         
            j += 1
    while i <= mid:
            q.append(arr[i])
            i += 1
    while j <= r:
            q.append(arr[j])
            j += 1

    # 把q里的元素复制到数组arr里去
    i,j = l,0
    while j < len(q):
        arr[i] = q[j]
        i += 1
        j += 1
    
    return res 

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print(merge_sort1(arr,0,len(arr)-1))
    #print(merge_sort(arr,0,len(arr)-1))
  
    
      
    