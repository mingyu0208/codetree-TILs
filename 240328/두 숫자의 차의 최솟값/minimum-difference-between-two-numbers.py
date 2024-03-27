n = int(input())
arr  = list(map(int,input().split()))
result = []

minus = max(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[j]-arr[i]<minus:
            minus = arr[j]-arr[i]
print(minus)