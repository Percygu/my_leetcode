def select_sort(arr):
    n = len(arr)
    for i in range(n):                 #   每次在剩下的元素中选择最小的元素放在arr[j]处
        for j in range(i,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]  # 保证a[i]是i到n元素中最小的
    return arr

if __name__ == "__main__":
    arr = [1,4,6,3,7,9,0,2,5,8]
    print(select_sort(arr))
