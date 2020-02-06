def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1          #  把第i个元素插入到钱0--i-1个排好序的序列中,从后往前比较，因为从后往前比较可以减少比较次数
        t = arr[i]
        while t < arr[j] and j >=0:
            arr[j+1] = arr[j]           #  元素后移,此时arr[i]会被覆盖，所以前面要把arr[i]用t存起来
            j -= 1
        arr[j+1] = t
    return arr

if __name__ == "__main__":
    arr = [4,1,6,3,7,9,0,2,5,8]
    print(insert_sort(arr))
        
            