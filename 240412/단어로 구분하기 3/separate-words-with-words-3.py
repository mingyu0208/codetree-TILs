arr = input().split()

for i in range(len(arr)-1,-1,-1):
    arr_len = len(arr)
    if arr_len<=100:
        print(arr[i])