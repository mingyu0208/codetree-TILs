n = int(input())
arr = list(map(int,input().split()))
min_val = arr[0]
cnt = 1

for i in range(1,n):
    if min_val > arr[i]:
        min_val = arr[i]
        cnt = 1
    elif min_val == arr[i]:
        cnt+=1

print(min_val,cnt )