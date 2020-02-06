def quick_sort(arr,l,r):
    if l >= r:
        return 
    x = arr[l]       # 在间随机选取一个数， 使得x左边的全部小于这个数，右边的全部大于这个数,这里选择区间的第一个数
    i,j = l,r 
    while i < j:
        while arr[j] >= x and i < j:         #  右边扫描
            j -= 1
        arr[i] = arr[j]
       
        while arr[i] <= x and i < j:         #  左边扫描
            i += 1 
        arr[j] = arr[i]
    
    arr[i] = x 
    quick_sort(arr,l,i)
    quick_sort(arr,i+1,r)
    return  arr


#   利用快排求逆序对


if __name__ == "__main__":
    arr = [1,4,6,3,7,9,0,2,5,8]
    print(quick_sort(arr,0,len(arr)-1))         
    
                      