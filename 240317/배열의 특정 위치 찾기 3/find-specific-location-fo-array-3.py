arr = list(map(int,input().split()))

sum_val = 0
n = len(arr)

for i in range(n):
    if arr[i]!=0:
        sum_val+=arr[i]
    if arr[i]==0:
        break
print(sum_val)